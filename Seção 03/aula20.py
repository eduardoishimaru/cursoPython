'''
primeiro_valor = input('Digite um valor: ')

segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print("primeiro_valor é maior que segundo_valor")
elif primeiro_valor < segundo_valor:
    print("segundo_valor é maior que primeiro_valor")
elif primeiro_valor == segundo_valor:
    print("primeiro_valor e segundo_valor são iguais")
else:
    print('Voce não digitou um número')
'''
    
    
    
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
    
