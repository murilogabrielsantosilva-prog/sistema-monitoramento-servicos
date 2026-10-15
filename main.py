from banco import salvar_checagem, criar_tabela, listar_checagens

import requests
from fastapi import FastAPI


def checar_servico_real(url, limite_lento=800):
    try:
        resposta = requests.get(url)
        tempo_ms = resposta.elapsed.total_seconds() * 1000

        if tempo_ms >= limite_lento:
            return f"LENTO | {tempo_ms:.0f} ms"
        else:
            return f"UP | {tempo_ms:.0f} ms"

    except requests.exceptions.RequestException:
        return "DOWN"


app = FastAPI()
criar_tabela()


@app.get("/")
def home():
    return {"mensagem": "Meu sistema de monitoramento está no ar!"}


sites_para_checar = [
    {"nome": "Google", "url": "https://www.google.com"},
    {"nome": "Youtube", "url": "https://www.youtube.com"},
    {"nome": "Netflix", "url": "https://www.netflix.com"},
]


@app.get("/status")
def status():
    resultados = []

    for site in sites_para_checar:
        status = checar_servico_real(site["url"])
        salvar_checagem(site["nome"], status)
        resultados.append({"nome": site["nome"], "status": status})

    return resultados


@app.get("/historico")
def historico():
    return listar_checagens()
