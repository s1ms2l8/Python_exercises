old_number = 0
new_number = 1

sequencia = str(old_number) + ',' + str(new_number)
digitos = 3

while digitos <= 30:
    next_number = old_number + new_number
    sequencia = sequencia + ',' + str(next_number)

    aux = next_number
    old_number = new_number
    new_number = aux
    digitos = digitos + 1

print(sequencia)
