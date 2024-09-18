# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from dados import produtos
import pprint
import copy


def p(v):
    pprint.pprint(v, sort_dicts=False, width=60)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


print(f'Aumento em 10% na lista')
produtos =[
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]
p(produtos)
print(f'_'*50)

print(f'DeepCopy')
novos_produtos = copy.deepcopy(produtos)
p(novos_produtos)
print(f'_'*50)

def exibir(lista):
    for item in lista:
        print(item)
    print(f'_'*50)


produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), reverse=False, key=lambda item: item['preco'])

produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), reverse=True, key=lambda item: item['nome'])


print(f'Organizado por nome: Decrescente')
exibir(produtos_ordenados_por_nome)

print(f'Organizado por preco: Crescente')
exibir(produtos_ordenados_por_preco)

