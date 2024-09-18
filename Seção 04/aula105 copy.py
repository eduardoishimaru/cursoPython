

def decoracao(func):
         
    def interna(x, y):
        try:
            x=float(x)
            y=float(y)
        except:
            print('numerus devem ser uma int ou float')
            return f'Digite apenas numeros'
        valida(x,y)
           
        return func(x , y)
    
    return interna


def valida(x, y):

        
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) :
       # raise TypeError('param deve ser uma int ou float')
       return False
    return x, y

@decoracao
def multiplica(x, y):
    #print(f'X={x} {type(x)}, Y={y} {type(y)}')
    return x * y
print(f'Multiplicação:')
numero_x = input(f'Número: ')
numero_y = input(f'Vezes o número: ')

#numero_x = float(numero_x)
#numero_y = float(numero_y)

print(f'{numero_x}X{numero_y}={multiplica(numero_x,numero_y):.2f}')