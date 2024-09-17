# Exercício - sistema de perguntas e respostas
import os
os.system('cls')
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

j = len(perguntas)
k = 0

contador_acertos = 0
while k < j:

    questao = perguntas[k]
    print(f'Pergunta: {questao['Pergunta']}')
    i=0
    for opcao in questao['Opções']:
        print(f'{i}) {opcao}')
        i+=1
    resposta = input(f'Escolha uma opção: ')
    resposta = int(resposta)
   
    if questao['Opções'][resposta] ==  questao['Resposta']:
        print(f'Acertou 👍')
        contador_acertos += 1
    else:
        print(f'Errou ❌')
        
    print(f'Questão {k}, Loop {j}')
    k += 1
    print(f'\n\n\n')
    
print(f'Você acertou {contador_acertos}')
print(f'de {j} perguntas.')
porcentagem_acertos = ((1/j) * contador_acertos)*100
print(f'{porcentagem_acertos:.2f}% de acerto!')
print(f'\n\n\n')