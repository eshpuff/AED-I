import sys
text = ["678"]
print("ponteiros ->",sys.getrefcount(text))
other = text
print(text,id(text))
print(other,id(other))
print("**")
print("ponteiros ->",sys.getrefcount(text))


print("------------------")
texto = ["A", "B", "C"] #mesmo endereço
outro = texto
print(texto,id(texto))
print(outro,id(outro))
print("**")
texto.append("tchau")
print(texto,id(texto))
print(outro,id(outro))

def incrementa(x): #imutável
    print(x,id(x))
    x[0] += 1
    print(x,id(x))

print("------------------")
x = [15]
print(x,id(x))
incrementa(x)
print(x,id(x))

