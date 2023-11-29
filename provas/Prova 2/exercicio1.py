'''Uma empresa de transporte oferece diferentes tarifas com base na distância percorrida em quilômetros e no tipo de veículo utilizado. Implemente um
programa em Python que solicite ao usuário a distância da viagem e o tipo de veículo, e calcule o valor total a ser pago. As informações sobre as tarifas estão
descritas a seguir: Ônibus: R$ 0,50 por Km; Carro: R$ 0,75 por Km; Moto: R$ 0,45 por Km. Além disso, a empresa oferece os seguintes descontos, dependendo da distância:
- Até 100 km: nenhum desconto.
- De 101 km a 300 km: 10% de desconto.
- Acima de 300 km: 20% de desconto.
Exemplo:
Digite a distância da viagem (em km): 250
Digite o tipo de veículo (ônibus, carro ou moto): carro
Valor total a ser pago: R$ 168,75'''

distancia = int(input("Digite a distÂncia da viagem (em km): "))
veiculo = input("Digite o tipo de veículo (ônibus, carro ou moto): ")
i = distancia
tarifa = 0


if veiculo == "ônibus":
    while i > 0:
        tarifa += 0.5   
        i -= 1
    print("Valor:",tarifa)

if veiculo == "carro":
    while i > 0:
        tarifa += 0.75
        i -= 1
    print("Valor:",tarifa)

if veiculo == "moto":
    while i > 0:
        tarifa += 0.45
        i -+ 1
    print("Valor:",tarifa)

if distancia > 101 and distancia < 300:
    desconto = 0.1 * tarifa
    tarifa = tarifa - desconto
    print ("Com desconto o valor a ser pago é:",tarifa)

if distancia > 300:
    desconto = 0.2 * tarifa
    tarifa = tarifa - desconto
    print ("Com desconto o valor a ser pago é:",tarifa)

