def processar_interacao(entrada, progresso):
    if len(progresso["interacoes"]) < 38:
        return "Verdades se escondem atrás de véus. O que você suspeita ser mentira?", "livre", False
    elif len(progresso["interacoes"]) == 38:
        return "O Oráculo encara você: 'Se pudesse saber toda a verdade sobre si mesmo, aceitaria?'", "reflexiva", False
    else:
        return "Aceitar a verdade é cruzar um abismo. Você atravessou.", "enigma", True
