from datetime import datetime


def get_time_summary() -> str:
    now = datetime.now()
    return f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


def search_web(query: str) -> str:
    return f"Search result for: {query} (mock result for now)."


def open_app(app_name: str) -> str:
    return f"Opening app: {app_name}"


def create_task(title: str, due_date: str | None = None) -> str:
    return f"Task created: {title} due {due_date or 'No due date'}"
