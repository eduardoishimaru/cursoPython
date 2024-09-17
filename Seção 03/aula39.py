import os
os.system('cls')
"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'


print("-"*100)
print(novo_nome)
print("-"*100)

##

'''
nome1 = 'Eduardo Tadashi'
nome2 = 'Janaina Nunes'


if len(nome1) > len(nome2):
    numero = len(nome1)
else:
    numero = len(nome2)

nome1 = nome1.zfill(numero)
nome2 = nome2.zfill(numero)

indice = 0
nomecancat =""
tamanho = numero - 1
tamanho = int(tamanho)
letra1 = ""
letra2 = ""

while indice < tamanho:
    letra1 = nome1[indice]
    letra2 = nome2[indice]
    nomecancat += f'*{letra1}*{letra2}'
    indice += 1

nomecancat += '*'

print(f'nome concatenado é, {nomecancat}')


'''