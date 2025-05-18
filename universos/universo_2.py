def processar_interacao(entrada, progresso):
    if len(progresso["interacoes"]) < 18:
        return "A culpa sussurra nas sombras. Você a escuta?", "direcionada", False
    elif len(progresso["interacoes"]) == 18:
        return "O Oráculo pergunta: 'O que você fez que nunca contou a ninguém?'", "reflexiva", False
    else:
        return "Você reconhece seus erros. Uma nova passagem se revela.", "enigma", True
