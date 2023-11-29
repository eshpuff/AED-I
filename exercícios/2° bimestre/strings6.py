'''Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
● Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
● Senha média: possui letras minúsculas, números e caracteres especiais, mas não possui letras maiúsculas.
● Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.'''

letra_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra_minuscula = "abcdefghijklmnopqrstuvwxyz"
numero = "0123456789"
simbolo = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
valida = 0
i = 0
i2 = 0
senha= input("Insira sua senha: ")

# while i != len(senha):
#     while valida != 1 and i2 < len(senha):
#         if senha[i] in letra_maiuscula:
#             valida += 1
#             i2 += 1
#     i += 1

# print(valida)