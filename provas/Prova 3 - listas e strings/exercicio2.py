'''O Instagram é uma popular plataforma de mídia social que permite aos usuários compartilhar fotos e vídeos. Considere um cenário em que você está desenvolvendo uma funcionalidade para analisar os comentários em postagens do Instagram. 
a) Escreva um código em Python que verifique se uma string comentário contém a menção a um usuário. Uma menção começa com o símbolo "@" seguido por um nome de usuário válido (composto apenas por letras minúsculas e números), por exemplo: "@usuario123".
b) Escreva um código em Python que substitua todas as menções a usuários na string comentário por "USUARIO_MENCIONADO".
c) Dado um conjunto de palavras proibidas, escreva um código em Python que verifique se a string comentário contém alguma das palavras proibidas. Se contiver, exiba "Conteúdo inadequado", caso contrário, exiba "Comentário permitido".'''

palavras_proibidas = ["oie", "palavras", "caixa", "português"]

string = input("Insira um comentário: ")
usuario = ""
comentario = ""
i = 0
cont = 0
palavra = ""
proibido = 0
arroba = 0

while i < len(string):
    if string[i] == "@":
        arroba +=1
    i += 1

if arroba != 0:
    print("possui menção.")
else:
    print("não possui menção")
i=0
while i < len(string):
    if string[i] == "@":
        comentario += "USUARIO_MENCIONADO "
        cont = i
        while string[cont] != " ":
            usuario += string[cont]
            cont += 1
        i = cont
    else:
        comentario += string[i]
    i += 1

lista1 = comentario.split()
i = 0

for i in lista1:
    if i in palavras_proibidas:
        proibido += 1

if proibido == 0:
    print("comentário permitido:",comentario)

else:
    print("comentário inadequado.")