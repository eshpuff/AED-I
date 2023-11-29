nome = input("Insira o nome: ")
matricula = input("Insira a matrícula: ")
nota = input("Insira a nota: ")

# arq = open('arquivo.txt',"r")
# # r = ler; w = gravar; a = append

#  # .read()
# texto = arq.read()
# print(texto)

# # .readline() ou .readlines()


# arq.close()

# # .write()
# arq = open("arquivo2.txt","w")
# texto = nome+";"+str(matricula)+";"+str(nota)+"\n"
# arq.write(texto)

# arq.close()

# .writelines()
arq = open("arquivo2.txt","w")
texto = nome+";"+str(matricula)+";"+str(nota)+"\n"
lista1 = [texto,"Augusto;162638;9"]
arq.writelines(lista1)

arq.close()