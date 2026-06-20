# NLP-Powered College Chatbot

## 📌 Overview
This is an **NLP-based chatbot** designed to provide basic information about Vaagdevi College of Engineering. It helps users get answers to frequently asked questions related to courses, facilities, admission, placements, and more.

## 🚀 Features
- **Smart NLP Matching**: Answers FAQs related to the college using TF-IDF and Cosine Similarity.
- **Premium UI**: Modern, responsive glassmorphism interface with dark/light mode support, chat bubbles, and typing indicators.
- **Always-On**: Deployed on **Render** with a self-ping background thread to prevent the free tier from sleeping.
- **Robust**: Includes a profanity filter, fallback responses, and health-check endpoints.
- **Persona Aware**: Capable of answering questions about itself and its creator.

## 🛠 Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **NLP:** scikit-learn (TF-IDF Vectorizer, Cosine Similarity), NumPy
- **Frontend:** HTML, CSS (Custom Properties for Theming), Vanilla JavaScript
- **Database:** JSON-like dictionary structure in `knowledge_base.py`
- **Deployment:** Render (Free Tier)

## 📂 Project Structure
```
NLP_chatbot/
│-- static/
│   ├── styles.css
│-- templates/
│   ├── index.html
│-- app.py
│-- knowledge_base.py
│-- requirements.txt
│-- Procfile
│-- README.md
```

## 🏗 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/srivardhan8919/NLP_chatbot.git
cd NLP_chatbot
```

### 2️⃣ Create & Activate a Virtual Environment
```sh
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Chatbot Locally
```sh
python app.py
```
Open your browser and go to `http://127.0.0.1:5000/`

---

## 🌐 Deployment on Render
### 1️⃣ Push Code to GitHub
```sh
git add .
git commit -m "Modernize UI and add keep-alive"
git push origin main
```

### 2️⃣ Deploy on Render
- Go to [Render](https://render.com/)
- Create a **new web service**
- Connect your GitHub repository
- Set the **Build Command**: `pip install -r requirements.txt`
- Set the **Start Command**: `gunicorn app:app --workers 2 --threads 2 --preload`
- The application will automatically detect its Render URL (via `RENDER_EXTERNAL_URL`) and ping itself every 14 minutes to prevent sleep.
- Deploy & Get Your Live URL 🎉

---

## 💡 Usage
1. Open the deployed link.
2. Toggle between Dark and Light mode using the sun/moon icon.
3. Enter your question about the college or click a suggested chip.
4. The chatbot will provide an accurate response based on the knowledge base.

---

## ✨ Contributing
Feel free to submit issues or pull requests to improve the chatbot.

---

## 📬 Contact
📧 **Email:** srivardhannani8919@gmail.com  
🔗 **GitHub:** [srivardhan8919](https://github.com/srivardhan8919)  
🔗 **LinkedIn:** [Sri Vardhan Nutenki](https://www.linkedin.com/in/sri-vardhan-nutenki-207b55249/)

---

### ⭐ If you found this helpful, give it a **star** on GitHub! ⭐
