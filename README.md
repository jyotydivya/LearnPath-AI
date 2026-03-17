# 🧠 AI Learning Path Generator

> **Generate personalised, step-by-step learning roadmaps for any topic — powered by Google Gemini.**

Enter a topic like *"Machine Learning"*, *"System Design"*, or *"Quantum Computing"* and get an AI-curated learning path complete with key concepts, resources, and project ideas — right in your browser.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Topic-based generation** | Type any subject and receive a structured learning roadmap |
| 🤖 **Gemini 1.5 Flash** | Uses Google's latest lightweight model for fast, high-quality responses |
| 🌐 **Simple web UI** | Clean, no-frills HTML interface — no build step required |
| 🔐 **Secure API key handling** | API key stays in a `.env` file, never committed to git |

---

## 🛠️ Tech Stack

- **Backend** — Python 3.9+ · Flask
- **AI** — Google Gemini via [`google-generativeai`](https://pypi.org/project/google-generativeai/)
- **Frontend** — Vanilla HTML + JavaScript (Fetch API)
- **Config** — `python-dotenv` for environment variable management

---

## 📁 Project Structure

```
.
├── app.py                 # Flask server + Gemini integration
├── templates/
│   └── index.html         # Frontend UI
├── requirements.txt       # Pinned Python dependencies
├── .env                   # API key (git-ignored)
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+**
- A **Google Gemini API key** — [Get one here](https://aistudio.google.com/app/apikey)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-learning-path-generator.git
cd ai-learning-path-generator
```

### 2. Create & activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

> [!IMPORTANT]
> Never commit your `.env` file. It is already included in `.gitignore`.

### 5. Run the app

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## 📡 API Reference

### `POST /generate-path`

Generate a learning path for a given topic.

**Request:**

```json
{
  "topic": "Quantum Computing"
}
```

**Success response** `200 OK`:

```json
{
  "learning_path": "## Step 1: Understand the Basics\n- Qubits vs classical bits\n..."
}
```

**Error response** `500 Internal Server Error`:

```json
{
  "error": "Failed to generate learning path."
}
```

---
