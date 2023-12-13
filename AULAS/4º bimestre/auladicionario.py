#Dicionário
dicio = {'chave': 'valor'} #criar um dicionario
dicio[chave] = valor #adicionar um item

valor = dicio["chave"] #retorna um valor dada uma chave
valor = dicio.get("chave","Não encontrou!") #retorna um valor dada uma chave

dicionario.values() #retorna todos valores
dicionario.keys() #retorna todas chaves 
dicionario.items() #retorna todos itens em tupla

dicio.update({'chave':'novo_valor'}) #atualiza valor

del dicio['chave'] #deleta um item pela chave
result = dicio.pop('chave') #exclusão dada a chave
result = dicio.popitem()   #exclusão do ultimo item



# fazer função adicionar_nota

# fazer função calcular_media

# fazer função consultar_nota_aluno

# Inicializar o dicionário de notas
notas = {}

# Adicionar notas
adicionar_nota(notas, "João", 8.5)
adicionar_nota(notas, "Maria", 7.0)
adicionar_nota(notas, "Carlos", 9.2)

# Calcular e imprimir a média geral
media_geral = calcular_media(notas)
print(f"Média Geral das Notas: {media_geral}")

# Consultar nota de um aluno específico
nota_maria = consultar_nota_aluno(notas, "Maria")
print(f"Nota de Maria: {nota_maria}")

# Consultar nota de um aluno que não existe
nota_pedro = consultar_nota_aluno(notas, "Pedro")
print(nota_pedro)  # Deve imprimir uma mensagem indicando que o aluno não foi encontrado