# A.H AI Assistant

A.H AI Assistant is a dark, futuristic personal AI project inspired by Jarvis-style helpers. The goal is to build an AI that can chat, automate tasks, send messages, search the web, coordinate reminders, and support future smart integrations.

## Features in this MVP
- FastAPI backend
- AI responder using OpenAI API (when configured)
- Dark red-black dashboard UI
- Chat interface
- Simple task and app automation endpoints

## Tech stack
- Python
- FastAPI
- OpenAI API
- HTML / CSS / JavaScript

## Project structure
- `backend/` — Python backend API
- `frontend/` — HTML/CSS/JS frontend interface

## Run locally

### 1) Create and activate a virtual environment
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Add your API key
Create a `.env` file in the project root with:
```env
OPENAI_API_KEY=your_key_here
```

### 4) Run backend
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5) Open frontend
Open `frontend/index.html` in a browser or serve it with a local web server.

## Example API requests
```bash
curl http://localhost:8000/
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message":"Hello A.H"}'
```

## Next roadmap
- Voice input/output
- Message integrations (WhatsApp, Telegram, SMS, email)
- Calendar and reminder integration
- App/script automation
- Personal memory and user profile
- Desktop app shell
