from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import knowledge_base
import datetime
import pytz
import threading
import time
import requests
import os

app = Flask(__name__)

# --- Profanity / Irregular Message Filter ---
PROFANITY_LIST = {"fuck", "shit", "bitch", "asshole", "stupid", "idiot", "dumb", "shut up"}

def contains_profanity(text):
    text_lower = text.lower()
    for word in PROFANITY_LIST:
        if word in text_lower:
            return True
    return False

# --- Keep-Alive Ping Thread ---
def keep_alive_ping():
    """Pings the Render URL every 14 minutes to prevent the service from sleeping."""
    # RENDER_EXTERNAL_URL is automatically provided by Render
    url = os.environ.get("RENDER_EXTERNAL_URL", "http://127.0.0.1:5000")
    if not url.startswith("http"):
        url = "https://" + url
    
    while True:
        try:
            time.sleep(14 * 60) # 14 minutes
            print(f"[{datetime.datetime.now()}] Sending keep-alive ping to {url}/health")
            requests.get(f"{url}/health", timeout=10)
        except Exception as e:
            print(f"Keep-alive ping failed: {e}")

# Start the background thread
ping_thread = threading.Thread(target=keep_alive_ping, daemon=True)
ping_thread.start()

def get_time_based_greeting():
    pz = pytz.timezone('Asia/Kolkata')
    current_hour = datetime.datetime.now(pz).hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"

greetings = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Ask me anything about the college.",
    "hey": "Hey! What would you like to know?",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! Feel free to ask any questions.",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you next time!",
    "see you": "Take care! Let me know if you need any help later."
}

persona_queries = {
    "who are you": "I am the Vaagdevi College Inquiry Chatbot! I'm an AI assistant here to help you with any information you need about courses, admissions, placements, facilities, and more.",
    "tell me about yourself": "I'm a natural language processing (NLP) chatbot designed to answer questions about Vaagdevi College of Engineering.",
    "who created you": "I was developed to assist students and visitors with their queries about Vaagdevi College.",
    "who made you": "I was developed to assist students and visitors with their queries about Vaagdevi College.",
    "what are you": "I'm an AI chatbot created to help you navigate information about Vaagdevi College of Engineering."
}

# Prepare the TF-IDF vectorizer using FAQ questions from knowledge base
# Flatten the questions array and keep track of answer index
flat_questions = []
answer_mapping = []

for idx, item in enumerate(knowledge_base.faq_data):
    for q in item["questions"]:
        flat_questions.append(q)
        answer_mapping.append(idx)

# This is computed once on startup and shared across requests
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
faq_matrix = vectorizer.fit_transform(flat_questions)

def get_chatbot_response(user_input):
    try:
        user_input_lower = user_input.lower().strip()
        
        # 1. Check for empty input
        if not user_input_lower:
            return "Please type a question."

        # 2. Check for profanity / irregular messages
        if contains_profanity(user_input_lower):
            return "Please maintain a respectful tone. Let me know if you have any questions about the college!"

        # 3. Check if the input is a greeting or farewell
        # We check exact match first for better accuracy, then fallback to partial
        if user_input_lower in greetings:
            return greetings[user_input_lower]
        
        for key, response in greetings.items():
            if user_input_lower.startswith(key):
                return response

        # 3.5 Check for persona questions (they often contain stop words that get ignored by TF-IDF)
        for key, response in persona_queries.items():
            if key in user_input_lower:
                return response

        # 4. Vectorize user input and compute similarity
        user_vec = vectorizer.transform([user_input])
        similarities = cosine_similarity(user_vec, faq_matrix).flatten()
        best_flat_idx = np.argmax(similarities)
        confidence = similarities[best_flat_idx]

        # 5. Confidence threshold check
        threshold = 0.35 # Slightly lowered for better matching with persona questions
        if confidence >= threshold:
            # Map the flat index back to the actual answer index
            answer_idx = answer_mapping[best_flat_idx]
            return knowledge_base.faq_data[answer_idx]["answer"]
        else:
            return "I'm sorry, I didn't quite catch that. Could you please rephrase your question?"
            
    except Exception as e:
        print(f"Error in chatbot processing: {e}")
        return "I encountered an error processing your request. Please try again."

@app.route("/")
def index():
    greeting_message = get_time_based_greeting()
    return render_template("index.html", greeting=greeting_message)

@app.route("/health")
def health_check():
    """Health check endpoint for keep-alive pings."""
    return jsonify({"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}), 200

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    if not data or "user_input" not in data:
        return jsonify({"error": "No user input provided"}), 400

    user_input = data["user_input"]
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
