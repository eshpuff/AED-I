# #Leia os 3 lados do triângulo e escreva se é um triangulo e que tipo de triangulo é (equilátero, isóceles ou escaleno)
# L1= float(input("Informe um dos lados do triângulo: "))
# L2= float(input("Informe o outro lado do triângulo: "))
# L3= float(input("Informe o último lado do triângulo: "))
# if (L1+L2) > L3 and (L1+L3) > L2 and (L2+L3) > L1:
#     print("É triangulo")
#     if L1 == L2 and L2 == L3:
#         print("É equilátero")
#     if (L1 == L2 and L2 != L3) or (L1 == L3 and L3 != L2)  or (L3 == L2 and L2 != L1):
#         print("É isóceles")
#     if (L1 != L2 and L2 !=L3) and (L1 != L3):
#         print("É escaleno")
# else:
#     print ("Não é triângulo.")

#Ler os três lados de um triângulo e por em ordem crescente
# L1= float(input("Informe um dos lados do triângulo: "))
# L2= float(input("Informe o outro lado do triângulo: "))
# L3= float(input("Informe o último lado do triângulo: "))

# if (L1+L2) > L3 and (L1+L3) > L2 and (L2+L3) > L1:
#     a=0
#     b=0
#     c=0
#     type = ""
#     if type= "equilátero":
#     a= L1
#     b= L2
#     c= L3
#     print("A-> "+ str(a))
#     print("B-> "+ str(b))
#     print("C-> "+ str(c))

#     if (L1 == L2 and L2 != L3) or (L1 == L3 and L3 != L2)  or (L3 == L2 and L2 != L1):
#         type= "isóceles"
#         if (L1 == L2 and L1 > L3):
#             a= L3
#             b= L2
#             c= L1
#             print("A-> "+ str(a))
#             print("B-> "+ str(b))
#             print("C-> "+ str(c))

#         if (L1 == L3 and L1 > L2):
#             a= L2
#             b= L1
#             c= L3
#             print("A-> "+ str(a))
#             print("B-> "+ str(b))
#             print("C-> "+ str(c))

#         else:
#             a= L1
#             b= L2
#             c= L3
#             print("A-> "+ str(a))
#             print("B-> "+ str(b))
#             print("C-> "+ str(c))

#     if (L1 != L2 and L2 !=L3) and (L1 != L3):
#         type= "escaleno"
# else:
    print("Não é trângulo.")


l1= float(input("Informe lado A: "))
l2= float(input("Informe lado B: "))
l3= float(input("Informe lado C: "))
if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    a=l1
    b=l2
    c=l3
    if b <= a and b<=c:
        tmp=a
        a=b
        b=tmp
    if c<=a and c<=b: 
        tbm= a 
        a = c 
        c = tmp
    if c <= b and c>=a:
        tmp=b 
        b = c 
        c = tmp
    print ("A->"+str(a))
    print ("B->"+str(b))
    print ("C->"+str(c))
else:
    print ("Não é triângulo.")