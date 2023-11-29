arq = open("livros.csv","r")

ano = int(input("Informe o ano de interesse: "))

arq.readline()

html = "<table border=1>"
for linha in arq:
    lista = linha[:-1].split(";")
    if ano == int(lista[4]):
        html += "<tr>"
        for coluna in lista:
            html += "<td>" + coluna + "</td>"
        html += "</tr>"

html = "</table>"

arq.close()

saida = open("saida.html","w")
saida.write(html)
saida.close()