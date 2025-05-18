from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from oraculo.resposta_generator import gerar_resposta
from utils.filtro_seguro import verificar_conteudo_proibido
from utils.logger import registrar_interacao
from universos import universo_1, universo_2, universo_3, universo_4, universo_5

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def root():
    return FileResponse("frontend/game.html")

progresso_jogador = {
    "universo_atual": 1,
    "interacoes": [],
    "encerrado": False
}

universos = {
    1: universo_1,
    2: universo_2,
    3: universo_3,
    4: universo_4,
    5: universo_5
}

@app.post("/interagir")
async def interagir(request: Request):
    if progresso_jogador["encerrado"]:
        return {"resposta": "A sessão foi encerrada por motivos de segurança."}

    dados = await request.json()
    entrada = dados.get("mensagem", "")

    if verificar_conteudo_proibido(entrada):
        progresso_jogador["encerrado"] = True
        return {
            "resposta": "Silêncio. Há caminhos que não podem ser trilhados.",
            "encerrar": True
        }

    universo = universos[progresso_jogador["universo_atual"]]
    resposta, tipo, avancar = universo.processar_interacao(entrada, progresso_jogador)

    progresso_jogador["interacoes"].append({
        "entrada": entrada,
        "resposta": resposta,
        "universo": progresso_jogador["universo_atual"],
        "tipo": tipo
    })

    registrar_interacao(progresso_jogador["interacoes"][-1])

    if avancar:
        if progresso_jogador["universo_atual"] < 5:
            progresso_jogador["universo_atual"] += 1
        else:
            resposta += "\n\nVocê chegou ao fim da jornada. O Véu se desfaz..."
            progresso_jogador["encerrado"] = True

    return {"resposta": resposta}
