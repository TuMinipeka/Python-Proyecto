from datetime import datetime

def log_evento(texto):
    with open("logs/eventos.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {texto}\n")
