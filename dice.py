import random

dado = int(input('numero do dado: '))

print(f'\nresultado do dado de {dado}: {random.randrange(1,dado)}')
