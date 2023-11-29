# 24) Dado o código abaixo, responda:
# Os endereços apresentados na tela são os mesmos? Por que?

str = "Algoritmo e Estrutura de "
print(str)
print("1o print - Endereço de str", id(str))
str += "Dados"
print(str)
print("2o print - Endereço de str", id(str))

# Não são iguais, pois quando concatenamos as duas strings
# uma nova string é criado e armazenada na memória, portanto não é o mesmo endereço.