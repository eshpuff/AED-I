# 22) Crie uma função em Python que receba por parâmetro uma lista e uma letra. Retorne
# uma lista equivalente à enviada como parâmetro, mas sem a letra informada. A ordem dos
# elementos deve ser mantida. Por exemplo:
# retira([a,b,c,a,f,a,a,k],a) —> [b,c,f,k]

def rewrite(list, letter):
    for i in list:
        if letter in i:
            list.remove(letter)
    return list
    
lista = ["a","b","a","d","a","f","a"]
rewrite(lista, "a")
print(lista)