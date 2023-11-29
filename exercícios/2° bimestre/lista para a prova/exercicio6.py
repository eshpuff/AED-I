'''Crie um programa que recebe uma string com letras maiusculas, espaços e números como entrada e retorna uma nova string em que cada caractere foi convertido para o código Morse. Exemplo: # Informe a mensagem: HELLO 123 # Saída esperada: ".... . .-.. .-.. ---   .---- ..--- ...--"'''
i = 0
morse = [".-", "-...","-.-.","-..",".","..'.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----"]
saida = ""

mensagem = input("Informe a mensagem: ").upper()

while i < len(mensagem):
    if mensagem[i] == "A":
        saida += morse[0]
        saida += " "
    if mensagem[i] == "B":
        saida += morse[1]
        saida += " "
    if mensagem[i] == "C":
        saida += morse[2]
        saida += " "
    if mensagem[i] == "D":
        saida += morse[3]
        saida += " "
    if mensagem[i] == "E":
        saida += morse[4]
        saida += " "
    if mensagem[i] == "F":
        saida += morse[5]
        saida += " "
    if mensagem[i] == "G":
        saida += morse[6]
        saida += " "
    if mensagem[i] == "H":
        saida += morse[7]
        saida += " "
    if mensagem[i] == "I":
        saida += morse[8]
        saida += " "
    if mensagem[i] == "J":
        saida += morse[9]
        saida += " "
    if mensagem[i] == "K":
        saida += morse[10]
        saida += " "
    if mensagem[i] == "L":
        saida += morse[11]
        saida += " "
    if mensagem[i] == "M":
        saida += morse[12]
        saida += " "
    if mensagem[i] == "N":
        saida += morse[13]
        saida += " "
    if mensagem[i] == "O":
        saida += morse[14]
        saida += " "
    if mensagem[i] == "P":
        saida += morse[15]
        saida += " "
    if mensagem[i] == "Q":
        saida += morse[16]
        saida += " "
    if mensagem[i] == "R":
        saida += morse[17]
        saida += " "
    if mensagem[i] == "S":
        saida += morse[18]
        saida += " "
    if mensagem[i] == "T":
        saida += morse[19]
        saida += " "
    if mensagem[i] == "U":
        saida += morse[20]
        saida += " "
    if mensagem[i] == "V":
        saida += morse[21]
        saida += " "
    if mensagem[i] == "W":
        saida += morse[22]
        saida += " "
    if mensagem[i] == "X":
        saida += morse[23]
        saida += " "
    if mensagem[i] == "Y":
        saida += morse[24]
        saida += " "
    if mensagem[i] == "Z":
        saida += morse[25]
        saida += " "
    if mensagem[i] == "1":
        saida += morse[26]
        saida += " "
    if mensagem[i] == "2":
        saida += morse[27]
        saida += " "
    if mensagem[i] == "3":
        saida += morse[28]
        saida += " "
    if mensagem[i] == "4":
        saida += morse[29]
        saida += " "
    if mensagem[i] == "5":
        saida += morse[30]
        saida += " "
    if mensagem[i] == "6":
        saida += morse[31]
        saida += " "
    if mensagem[i] == "7":
        saida += morse[32]
        saida += " "
    if mensagem[i] == "8":
        saida += morse[33]
        saida += " "
    if mensagem[i] == "9":
        saida += morse[34]
        saida += " "
    if mensagem[i] == " ":
        saida += "  "
    i += 1

print(saida)