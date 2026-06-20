# NLP-Powered College Chatbot

## 📌 Overview

This is an **NLP-based chatbot** engineered specifically for Vaagdevi College of Engineering. It acts as an intelligent assistant, answering a wide variety of queries regarding admission processes, branch details, hostel facilities, campus infrastructure, fee structures, and placement statistics using real-world data.

## 🚀 Features

- **Optimized Multi-Variation NLP Matching**: Employs a custom, memory-efficient TF-IDF array-mapping algorithm that accurately understands synonyms and different question phrasings without needing heavy deep-learning models.
- **Premium Immersive UI**: A state-of-the-art frontend featuring glassmorphism, animated pure CSS SVG waves (zero GPU overhead), inline SVG iconography, and persistent dark/light mode.
- **Render-Optimized Anti-Sleep**: Contains a daemonized background thread that detects the live `RENDER_EXTERNAL_URL` and pings itself every 14 minutes, completely bypassing free-tier sleep limits.
- **Robust Edge Handling**: Includes a profanity filter, dynamic fallback responses, and time-aware greeting endpoints.
- **Persona & Context Aware**: Equipped with specific routing to answer conversational questions about its identity and creator seamlessly.

## 🛠 Tech Stack

- **Backend:** Python, Flask, Gunicorn (Multi-threaded worker config)
- **NLP:** scikit-learn (TF-IDF Vectorizer, Cosine Similarity), NumPy
- **Frontend:** HTML5, CSS3 (Native SVG Animations, Theming), Vanilla JavaScript
- **Database:** Array-mapped JSON-like structure via `knowledge_base.py`
- **Deployment:** Render (Free Tier Optimized)

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

---

### ⭐ If you found this helpful, give it a **star** on GitHub! ⭐
