# 23) Dado o código abaixo, responda:
# a) Os endereços apresentados na tela das variáveis nos 1o e 2o prints são iguais? Por que?
# b) De acordo com a resposta no item (a), qual será o endereço apresentado no 3o print do
# código?

x = 10
y = 10
print("x = ", x, "\n")
print("1o print - Endereço de x", id(x))
print("2o print - Endereço de y", id(y))
x -= 1
print("x = ", x, "\n")
print(x)
print("3o print - Endereço de x", id(x))