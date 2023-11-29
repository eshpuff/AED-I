'''Crie um programa que leia uma string e um número inteiro como chave e retorne uma nova string em que cada caractere foi deslocado para a direita na sequência de caracteres ASCII pelo valor da chave.  Exemplo: # Informe a mensagem: hello # Informe a chave: 3 # Saída esperada: "khoor" '''

saida = ""

mensagem = input("Informe a mensagem: ")
chave = int(input("Informe a chave: "))

for i in mensagem:
    codigo = ord(i) + chave
    caractere = chr(codigo)
    saida += caractere

print("Saída esperada:", saida)
