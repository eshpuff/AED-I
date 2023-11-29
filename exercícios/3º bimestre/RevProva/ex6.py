'''6) Faça um programa em Python que leia duas listas de números compostas por cinco
elementos informados de maneira ordenada (números em ordem crescente). Crie uma
terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
soma dos seus elementos contidos.'''

def inputs():

    list1 = []
    list2 = []

    for i in range(5):
        value1 = int(input(f"Insert the {i + 1}º number: "))
        list1.append(value1)
        list1.sort()

    for i in range(5):
        value2 = int(input(f"Insert the {i + 1}º number (second list): "))
        list2.append(value2)
        list2.sort()

    return list1, list2

def sz(list1,list2):
    list3 = sorted(list1 + list2)
    return list3

def results():
    list1, list2 = inputs()
    list3 = sz(list1,list2)
    
    print(f'This is the first list: {list1}')
    print(f'This is the second list: {list2}')
    print(f'This is the third list {list3}')
    print(f'Value when theyre together:', sum(list3))
results()




