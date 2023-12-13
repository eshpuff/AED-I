def adicionarProduto(estoque,nomeProduto,quantidade):
    if nomeProduto in estoque:
        estoque[nomeProduto] += quantidade
    else:
        estoque[nomeProduto] = quantidade

def venderProduto(estoque, nomeProduto, quantidade):
    if nomeProduto in estoque:
        if estoque[nomeProduto] >= quantidade:
            estoque[nomeProduto] -= quantidade
            print(f"Compra de {quantidade} {nomeProduto}(s) realizada.")
        else:
            print("Não foi possivel efetuar compra. Estoque insuficiênte.")
    else:
        print(f"{nomeProduto} não disponível.")

def relatorioEstoque(estoque):
    print(estoque)


estoque = {"chiclete": 100}

adicionarProduto(estoque, 'bala', 130)
adicionarProduto(estoque, "chiclete", 54)
venderProduto(estoque, "chiclete", 3)
venderProduto(estoque, "chocolate", 6)
relatorioEstoque(estoque)