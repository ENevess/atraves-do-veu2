def processar_interacao(entrada, progresso):
    if len(progresso["interacoes"]) < 28:
        return "Diante de três portas: Qual escolhe? Esquerda, Centro ou Direita?", "direcionada", False
    elif len(progresso["interacoes"]) == 28:
        return "O Oráculo diz: 'Cada escolha te molda mais do que pensa. Qual foi a sua pior?'", "reflexiva", False
    else:
        return "Você decide com clareza. O próximo universo aguarda.", "enigma", True
