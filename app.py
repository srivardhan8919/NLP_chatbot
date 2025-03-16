from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import knowledge_base
import datetime

app = Flask(__name__)

def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 21:
        return "Good evening"
    else:
        return "Good evening"

greetings = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! Ask me anything about the college.",
    "hey": "Hey! What would you like to know?",
    "good morning": "How can I assist you today?",
    "good afternoon": "How can I help?",
    "good evening": "Feel free to ask any questions.",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you next time!",
    "see you": "Take care! Let me know if you need any help later."
}

# Prepare the TF-IDF vectorizer using FAQ questions from knowledge base
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
faq_matrix = vectorizer.fit_transform(knowledge_base.faq_questions)

def get_chatbot_response(user_input):
    user_input_lower = user_input.lower()
    
    # Check if the input is a greeting or farewell
    for key in greetings.keys():
        if key in user_input_lower:
            return greetings[key]

    # Vectorize user input
    user_vec = vectorizer.transform([user_input])
    
    # Compute cosine similarity with the FAQ matrix
    similarities = cosine_similarity(user_vec, faq_matrix).flatten()
    best_idx = np.argmax(similarities)
    confidence = similarities[best_idx]

    # Confidence threshold
    threshold = 0.4
    if confidence >= threshold:
        return knowledge_base.faq_answers[best_idx]
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

@app.route("/")
def index():
    greeting_message = get_time_based_greeting()
    return render_template("index.html", greeting=greeting_message)

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