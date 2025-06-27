# 🧠 TailorTalk - Smart Meeting Scheduler

TailorTalk is an AI-powered conversational assistant that helps you **book and check Google Calendar events** using natural language. Built using FastAPI, Google Calendar API, LangGraph-style flow logic, and Streamlit frontend.

---

## 🚀 Live Deployment Links

- 🌐 **Frontend UI (Streamlit):** [https://tailortalk-ui.streamlit.app](https://tailortalk-ui.streamlit.app)
- ⚙️ **Backend API (FastAPI on Render):** [https://tailortalk-final.onrender.com](https://tailortalk-final.onrender.com)
- 📁 **GitHub Repo:** [https://github.com/Denim-coder/tailortalk-final](https://github.com/Denim-coder/tailortalk-final)

---

## 📦 Project Structure

tailortalk/
├── backend/ # FastAPI backend
│ ├── main.py # API entrypoint
│ ├── agent.py # Chat logic
│ └── calendar_utils.py # Google Calendar integration
├── frontend/ # Streamlit UI
│ └── app.py
├── requirements.txt # Shared dependencies
├── render.yaml # Render deployment config
├── .gitignore # Hides sensitive files
└── README.md # This file

yaml
Copy
Edit

---

## 🧠 Features Implemented (per assignment)

- ✅ Natural language meeting booking (e.g. "Book a meeting tomorrow at 4 PM")
- ✅ Free/busy time checker (e.g. "Am I free next Friday?")
- ✅ Google Calendar integration using service account
- ✅ LangGraph-like conditional flow logic
- ✅ Full Streamlit frontend interface
- ✅ Secure credentials via Render environment variables
- ✅ Deployable with `render.yaml`
- ✅ `requirements.txt` included for cloud builds

---

## 🛠 Local Development (optional)

1. Clone the repo:
   ```bash
   git clone https://github.com/Denim-coder/tailortalk-final.git
   cd tailortalk-final
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run backend:

bash
Copy
Edit
uvicorn backend.main:app --reload
Run frontend:

bash
Copy
Edit
streamlit run frontend/app.py
🔐 Important Notes
Google credentials are securely loaded via GOOGLE_CREDENTIALS_JSON environment variable on Render.

The actual service_account.json is excluded from the repo via .gitignore.

🙌 Author
Made with 💻 and ☕ by Denim-coder

yaml
Copy
Edit

---

### 📌 What to do with it?

- Save it as `README.md` in the root of your project folder
- Commit & push it:
```bash
git add README.md
git commit -m "📝 Added final README for submission"
git push origin main