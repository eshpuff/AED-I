'''Faça um programa em python que leia 3 números e os mostre em ordem crescente.'''

l1= float(input("Informe lado A: "))
l2= float(input("Informe lado B: "))
l3= float(input("Informe lado C: "))

a = l1
b = l2
c = l3

if b <= a and b <= c:
    tmp = a
    a = b
    b = tmp
if c <=a and c <= b: 
    tmp = a 
    a = c 
    c = tmp
if c <= b and c >= a:
    tmp = b 
    b = c 
    c = tmp

print ("A->"+ str(a))
print ("B->",b)
print ("C->",c)