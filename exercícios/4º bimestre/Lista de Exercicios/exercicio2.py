def atualizarMedalhas(pais, medalha, quantidade):
    pais[medalha] += quantidade

def relatorioMedalhas(pais):
    print(pais)

paisA = {"ouro": 0, "prata": 0, "bronze": 0}
paisB = {"ouro": 0, "prata": 0, "bronze": 0}


atualizarMedalhas(paisA, "prata", 10)
atualizarMedalhas(paisA, "ouro", 2)
atualizarMedalhas(paisA, "bronze", 100)

atualizarMedalhas(paisB, "ouro", 4)
atualizarMedalhas(paisB, "prata", 12)
atualizarMedalhas(paisB, "bronze", 92)


relatorioMedalhas(paisA)
relatorioMedalhas(paisB)