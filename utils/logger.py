import json
from datetime import datetime

def registrar_interacao(dados):
    with open("logs/interacoes_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps({**dados, "timestamp": datetime.now().isoformat()}) + "\n")
