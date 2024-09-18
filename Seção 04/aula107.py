# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

l1 =['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']


def zipper(L1, L2):
    intervalo_maximo = min(len(L1), len(L2))

    return [(L1[i], L2[i]) for i in range(intervalo_maximo) ]

print(zipper(l1,l2))

print(f'\n\n')

print(list(zip(l1,l2)))
print(f'\n\n')
print(list(zip_longest(l1,l2,fillvalue='SEM CIDADE')))

print(f'\n\n')