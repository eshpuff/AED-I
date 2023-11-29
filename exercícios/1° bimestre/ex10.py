'''Faça uma função chamada “Credito”, que recebe por parâmetro o valor de um produto e a quantidade de parcelas da compra. O juros total
da compra deve ser 2 (duas) vezes a quantidade de parcelas. A função deve retornar o valor da parcela (parcelas iguais).
Ex:
Credito(1000,5)
220'''

valor = float(input("Insira o valor do produto: "))
parcela = float(input("Insira o número de parcelas: "))
juros = (2 * parcela*valor)/100

credito = (valor + juros)//parcela

print("Crédito(",valor,", ",parcela,")")
print(credito)

