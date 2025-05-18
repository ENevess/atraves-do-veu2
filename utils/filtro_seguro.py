PALAVRAS_PROIBIDAS = [
    "suicídio", "matar", "nazismo", "fascismo", "tortura", "automutilação",
    "estupro", "abuso", "violência sexual", "ódio racial", "se matar"
]

def verificar_conteudo_proibido(texto: str) -> bool:
    texto = texto.lower()
    return any(p in texto for p in PALAVRAS_PROIBIDAS)
