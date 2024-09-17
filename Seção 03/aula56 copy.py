"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""


'''
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)


'''

frase = '    Olha que coisa   , mais linda    , mais cheia de graça     '
lista_frases_cruas = frase.split(', ')

#print(f'{lista_frases_cruas}')

lista_frases=[]
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
print(f'\n \n')
print(f'lista_frases_cruas= {lista_frases_cruas} \n \n')
print(f'lista_frases= {lista_frases} \n \n')
frases_unidas = ', '.join(lista_frases)
print(f'Join frases unidas = {frases_unidas} \n \n')