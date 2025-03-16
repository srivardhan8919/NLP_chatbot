# NLP-Powered College Chatbot

## 📌 Overview
This is an **NLP-based chatbot** designed to provide basic information about Vaagdevi College of Engineering. It helps users get answers to frequently asked questions related to courses, facilities, admission, placements, and more.

## 🚀 Features
- Answer FAQs related to the college
- NLP-based response generation
- Deployed on **Render** for public access
- Interactive web interface with **Flask & HTML/CSS**

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **NLP:** Natural Language Processing (NLTK, spaCy)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** JSON-based knowledge base
- **Deployment:** Render (Free Tier)

## 📂 Project Structure
```
NLP_Clg_chat_bot/
│-- static/
│   ├── styles.css
│-- templates/
│   ├── index.html
│-- app.py
│-- knowledge_base.py
│-- requirements.txt
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
git commit -m "Initial commit"
git push origin main
```

### 2️⃣ Deploy on Render
- Go to [Render](https://render.com/)
- Create a **new web service**
- Connect your GitHub repository
- Set the **Build Command**: `pip install -r requirements.txt`
- Set the **Start Command**: `python app.py`
- Deploy & Get Your Live URL 🎉

---

## 💡 Usage
1. Open the deployed link.
2. Enter your question about the college.
3. The chatbot will provide an accurate response.

---

## 🛠 Troubleshooting
- If Flask doesn’t start, check the Python version (`python --version`).
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- If deployment fails on Render, check logs for errors.

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
