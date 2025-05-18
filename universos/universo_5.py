def processar_interacao(entrada, progresso):
    if len(progresso["interacoes"]) < 48:
        return "Você caminha por um espelho. Quem você é agora?", "livre", False
    elif len(progresso["interacoes"]) == 48:
        return "O Oráculo finaliza: 'Você é quem chegou até aqui, mas... quem começou?' ", "reflexiva", False
    else:
        return "Identidade revelada. A jornada termina. Ou recomeça.", "enigma", True
