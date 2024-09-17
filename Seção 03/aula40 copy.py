""" Calculadora com while """
import os
import time 
while True:
    os.system('cls')

    print('Calculadora')

    try:
        numero1 = input(f"Digite o primeiro número: ")
        numero1 = float(numero1)
        numero2 = input(f"Digite o segundo número: ")
        numero2 = float(numero2)
    except:
        print(f'Digite um numero não uma letra')
        time.sleep(2)
        continue
        


    print(f'Escolha a operção: ')
    print(f'Adição = + ')
    print(f'Subtração = -')
    print(f'Divisão = /')
    print(f'Multiplicação = *')
    
        
    operacao = input()
    
    operadores = '+-/*'
    if operacao not in operadores:
        print('Digite somente um operador valido! ')
        time.sleep(2)
        continue
    if len(operacao) > 1:
        print('Digite somente um operador valido! ')
        time.sleep(2)
        continue
    
    if operacao == "+":
        resultado = numero1 + numero2
        print(resultado)
    elif operacao == "-":
        resultado = numero1 - numero2
        print(resultado)
    elif operacao == "/":
        resultado = numero1 / numero2
        print(resultado)
    elif operacao == "*":
        resultado = numero1 * numero2
        print(resultado)
    else:
        print(f'Operação invalida!')
    saida = input("Deseja sair? S/N: ").lower().startswith('s')
    if saida:
        os.system('cls')
        break
