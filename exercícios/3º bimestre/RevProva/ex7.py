'''7) Altere o programa anterior para desprezar os números iguais, caso estes existam.
Portanto, a lista final não deve possuir números iguais armazenados.'''

def inputs():

    list1 = []
    list2 = []
    cont1 = 1
    cont2 = 1

    while cont1 <= 6:
        value1 = int(input(f"Insert the {cont1}º number (first list): "))
        if value1 not in list1:
            list1.append(value1)
            cont1 += 1
        else:
            print("This value is already in list. Insert another one.")

    list1.sort()

    while cont2 <= 6:
        value2 = int(input(f"Insert the {cont2}º number (second): "))
        if value2 not in list2:
            list2.append(value2)
            cont2 += 1
        else:
            print("This value is already in list. Insert another one.")

    list2.sort()

    return list1, list2

def sz(list1,list2):

    list3 = []
    
    for num in list1 + list2:
        if num not in list3:
            list3.append(num)
    
    list3.sort()
    return list3
    
def results():
    list1, list2 = inputs()
    list3 = sz(list1,list2)
    
    print(f'This is the first list: {list1}')
    print(f'This is the second list: {list2}')
    print(f'This is the third list: {list3}')
    print(f'Value when theyre together:', sum(list3))
results()