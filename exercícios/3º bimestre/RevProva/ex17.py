# 17) Crie as seguintes listas derivadas da lista informada:
# L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# ● Intervalo de 1 a 9
# ● Intervalo de 8 a 13
# ● Números pares
# ● Números ímpares
# ● Lista reversa

l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

oneToNine = []
eightToThirteen = []
evenNumbers = []
oddNumbers = []
inverse = []


for i in range(l.index(1),l.index(10)):
    oneToNine.append(i)
    
for i in range(l.index(8),l.index(13)):
    eightToThirteen.append(i)
    
for i in l:
    if i%2 == 0 or i == 0:
        evenNumbers.append(i)
    else:
        oddNumbers.append(i)
    
cont = len(l)-1

for i in l:
    inverse.append(l[cont])
    cont -= 1    
    