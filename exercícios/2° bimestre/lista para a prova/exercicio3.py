'''Crie 3 listas que contém o nome de um produto, o seu preço e a quantidade disponível em estoque. Peça ao usuário para comprar um produto digitando o nome e a quantidade desejada. Verifique se o produto está disponível em estoque e, se estiver, atualize a quantidade disponível e informe o total a pagar. Repita esse processo até que o usuário digite "sair".'''

produto = ["cerveja","vinho","corote"]
preço = [3.90,20,5.10]
estoque = [150, 48, 3]
valor_cerveja = 0
valor_vinho = 0
valor_corote = 0

menu = input("Bem vindo! Digite 1 caso queira saber quais produtos catalogados. \n Digite 2 caso queria realizar uma compra. \n Digite sair para finalizar.\n Resposta: ").lower()

while menu != "sair":
    if menu == "1":
        print("Nosso catálogo conta com:", produto)
    if menu == "2":
        compra = input("Insira o nome do produto desejado: ").lower()
        if compra in produto:
            if compra == "cerveja":
                print("Temos",estoque[0],"itens no estoque.")
                quantidade_cerveja = int(input("Insira quantidade de latas de cerveja a serem compradas: "))
                if int(estoque[0]) != 0:
                    estoque[0] -= quantidade_cerveja
                    if estoque[0] < 1:
                        produto.remove("cerveja")
                        print("Erro. Quantidade indisponível")
                    else:
                        valor_cerveja = preço[0] * quantidade_cerveja
            if compra == "vinho":
                print("Temos",estoque[1],"intens no estoque.")
                quantidade_vinho = int(input("Insira a quantidade de garrafas de vinho a serem compradas: "))
                if int(estoque[1]) != 0:
                    estoque[1] -= quantidade_vinho
                    if estoque[1] < 0:
                        produto.remove("vinho")
                        print("Erro. Quantidade indisponível")
                    else:
                        valor_vinho = preço[1] * quantidade_vinho
            if compra == "corote":
                print("Temos",estoque[2],"intens no estoque.")
                quantidade_corote = int(input("Insira a quantidade de garrafas de corote a serem compradas: "))
                if int(estoque[2]) != 0:
                    estoque[2] -= quantidade_corote
                    if estoque[2] < 0:
                        produto.remove("corote")
                        print("Erro. Quantidade indisponivel.")
                    else:
                        valor_corote = preço[2] * quantidade_corote
            valor_total = valor_vinho + valor_cerveja + valor_corote
            print("O valor total da sua compra é de R$:",valor_total)
    menu = input("Caso queira adicionar mais itens ao seu carrinho digite 2. \n Digite sair para finalizar. \n Resposta: ").lower()
if menu == "sair":
    print("Obrigado por comprar conosco, volte sempre.")