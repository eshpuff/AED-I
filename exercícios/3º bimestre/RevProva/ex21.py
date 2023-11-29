# 21) Crie uma função em Python que receba por parâmetro uma string e uma letra. Retorne a
# string equivalente à enviada como parâmetro, mas sem a letra informada. Por exemplo:
# retira(“Antonia Piedade”,”a”) —> “ntoni Piedde”
# ● Crie a função usando qualquer recurso Python, como split, search e etc;
# ● Crie a função usando apenas recursos básicos, sem as funções para manipulação de
# strings.

def rewrite(string, letter):
    return string.replace(letter,"")

def rewriteBasic(string, letter):
    new = ""
    for i in string:
        if i != letter:
            new+=i
    return new
    
string = "barbara"

print(rewriteBasic(string, "a"))
print(rewrite(string, "a"))

    