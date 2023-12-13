def decimalParaBinario(arrayBinario, decimal):
    if decimal == 0:
        arrayBinario.append(0)
    else:
        while decimal > 0:
            resto = decimal % 2
            arrayBinario.insert(0, resto)
            decimal = decimal // 2 

arrayBinario = []
numeroDecimal = 25

decimalParaBinario(arrayBinario, numeroDecimal)

print("A representação binária é: ", arrayBinario)
