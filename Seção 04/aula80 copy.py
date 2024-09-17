"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
import time
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# s1 = lista_de_listas_de_inteiros[0]
# print(s1)


# for lista in lista_de_listas_de_inteiros:
#     s1 = lista
#     s2 = set()
#     s3 = set()
#     for numero in s1:
#         if numero not in s2:
#             s2.add(numero)
            
#         else:
#             s3.add(numero)
#             break
#     if s3 == set():
#         s3.add(-1)

#     print(f'Lista {s1} , {s3}')
# time.sleep(2)
# print(f'\n\n\n')

def encontraDuplicado(lista):
    checklista = set()
    primeiroDuplicado = -1
    for validaNumero in lista:
        if validaNumero in checklista:
            primeiroDuplicado = validaNumero
            break
        
        checklista.add(validaNumero) 
    
    return primeiroDuplicado

for lista in lista_de_listas_de_inteiros:
    duplicado = encontraDuplicado(lista)
    print(f'{lista} // {duplicado}')
    