"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'
cpf_sem_ponto =[]
for num in cpf:
    try: 
        if num == "." or num =="-":
            continue
        int(num)
        cpf_sem_ponto.append(num)
    except:
        ...
        
print(cpf_sem_ponto)    

cpf_sem_digito = []


#Parte 2 multiplicar todos de 10 a 2
multiplicado =[]
multiplicacao = int(10)
for num in cpf_sem_ponto:   
    if multiplicacao == 1:
        break
    else:
        result= int(num) * multiplicacao
        multiplicado.append(result)
        multiplicacao -= 1


print(multiplicado)
#Parte 3 somando os numeros

soma = int()
for num in multiplicado:
    soma += int(num)

print(soma)

#Parte 4 multiplicar por 10
multi10 = soma * 10

print(multi10)

#Parte 5 se for maior que 9 o valor deve ser 0
valor = multi10 % 11

if valor > 9:
    valor = 0
else:
    print(valor)

print(f'O primeiro digito do CPF é {valor}')



