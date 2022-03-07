num = int(input('Insira um número:'))
primo = True
I = 2

while I < num:
    if (num % I) == 0:
        primo = False

    I = I + 1

print(primo)
