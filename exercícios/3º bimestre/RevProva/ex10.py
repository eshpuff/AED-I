txt = input("Write a whole text if you want: ")

def spacebar(txt):

    current = 0
    max = 0

    for words in txt:
        if words == ' ':
            current += 1
        else:
            if current > max:
                max = current
            current = 0
    return max

max = spacebar(txt)

print(f"The longest spacebar pressed here was {max}.")