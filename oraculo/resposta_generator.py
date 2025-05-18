import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(entrada):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um oráculo enigmático que responde com frases misteriosas, reflexivas e simbólicas. Fale sempre como se estivesse guiando alguém por uma jornada espiritual ou existencial."},
            {"role": "user", "content": entrada}
        ],
        temperature=0.9,
        max_tokens=250
    )
    return resposta.choices[0].message.content.strip()
