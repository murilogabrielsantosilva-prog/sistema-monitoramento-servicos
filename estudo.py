servicos = [
    {"nome": "Google", "tempo_resposta": 180},
    {"nome": "Youtube", "tempo_resposta": 1200},
    {"nome": "Netflix", "tempo_resposta": 100},
    {"nome": "Whatsapp", "tempo_resposta": 1400},
    {"nome": "Site fora do ar", "tempo_resposta": None},
    {"nome": "Servico bugado"},
    {"nome": "Servico estranho", "tempo_resposta": "rápido"}
]

limite_lento = 800


def verificar_servico(servico, limite_lento):
    try:
        tempo = servico["tempo_resposta"]
        if tempo is None:
            return "DOWN"
        elif tempo >= limite_lento:
            return f"LENTO | {tempo} ms"
        else:
            return f"UP |{tempo} ms"
    except KeyError:
        return "ERRO: dado invalido"
    except TypeError:
        return "Erro: tipo de dado invalido"
    except Exception as e:
        return f"ERRO: {e}"


for servico in servicos:
    resultado = verificar_servico(servico, limite_lento)
    print(f"{servico['nome']}: {resultado}")
