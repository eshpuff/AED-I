'''Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial, em gramas, faça um programa 
em Python que determine o tempo necessário para que essa massa se torne menor que 0,05 gramas.'''

massa = float(input("Insira massa incial em gramas: "))
i = 0

while massa > 0.05:
    massa = massa / 2
    i += 50

print("O tempo é",i,"segundos")