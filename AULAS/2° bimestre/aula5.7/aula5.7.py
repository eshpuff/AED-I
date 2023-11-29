''' Criar um bag of words e calcular a frequência de cada palavra. '''

import re
texto = '''I'm tired of being what you want me to be
Feeling so faithless, lost under the surface
Don't know what you're expecting of me
Put under the pressure of walking in your shoes
Every step that I take is another mistake to you
(Caught in the undertow, just caught in the undertow)
I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
Can't you see that you're smothering me
Holding too tightly, afraid to lose control?
'Cause everything that you thought I would be
Has fallen apart right in front of you
Every step that I take is another mistake to you
(Caught in the undertow, just caught in the undertow)
And every second I waste is more than I can take
I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
And I know
I may end up failing too
But I know
You were just like me with someone disappointed in you
I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
I've become so numb
I can't feel you there
(I'm tired of being what you want me to be)
I've become so numb
I can't feel you there
(I'm tired of being what you want me to be)'''.lower()

novo_texto = re.sub(r"[!@#-$,'.()]",'',texto)

lista = novo_texto.split()
frequencia = []
lista_final = []
i = 0
cont = 0

# print(lista)

while i < len(lista):
    if lista[i] in lista_final:
        posicao= lista_final.index(lista[i])
        frequencia[posicao] += 1
    else:
        lista_final.append(lista[i])
        frequencia.append(1)
    i += 1
# print(lista_final)
# print(frequencia)

print("Termos : frequencia")
while cont < len(lista_final):
    porcentagem = (frequencia[cont]/len(lista)) * 100
    print(lista_final[cont]+":",frequencia[cont])
    # print(lista_final[cont]+":",porcentagem,"%")
    cont += 1

#saida.csv