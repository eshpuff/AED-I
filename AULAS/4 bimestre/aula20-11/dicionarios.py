dicio = {'chave': 'valor'} # criar um dicionario
dicio[chave] = valor #adicionar um item

valor = dicio["chave"] # retorna um valor dada uma chave
valo = dicio.get("chave", "Não encontrou!") # retorna um valor dada uma chave

dicionario.values() #retorna todos valores
dicionario.keys() # retorna todas chaves
dicionario.items() # retorna todos itens

dicio.update({'chave': 'novoValor'}) #atualiza o valor

del dicio['chave'] #deleta um item pela chave

result = dicio.pop('chave') #exclusão dada a chave
result = dicio.popitem() #exclusão do último item
