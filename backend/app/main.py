from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.assistant import chat_with_ai
from app.tools import get_time_summary, search_web, open_app, create_task

app = FastAPI(title="A.H AI Assistant", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "app": "A.H AI Assistant",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    reply = chat_with_ai(req.message)
    return {"reply": reply}


@app.get("/time")
def time_route():
    return {"result": get_time_summary()}


@app.get("/search")
def search_route(query: str):
    return {"result": search_web(query)}


@app.get("/open-app")
def open_app_route(app_name: str):
    return {"result": open_app(app_name)}


@app.get("/task")
def task_route(title: str, due_date: str | None = None):
    return {"result": create_task(title, due_date)}
