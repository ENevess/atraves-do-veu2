def processar_interacao(entrada, progresso):
    if len(progresso["interacoes"]) < 8:
        return "Você ouve ecos de lembranças distantes...", "livre", False
    elif len(progresso["interacoes"]) == 8:
        return "O Oráculo te desafia: 'O que você mais teme esquecer?'", "reflexiva", False
    else:
        return "Você enfrentou seu passado. O Véu se abre para o próximo caminho.", "enigma", True
