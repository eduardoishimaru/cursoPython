# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
        
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quaduplicar = criar_multiplicador(4)
decplicar = criar_multiplicador(10)

print(f'Duplicado {duplicar(2)}')
print(f'Triplicado {triplicar(2)}')
print(f'Quadruplicado {quaduplicar(2)}')
print(f'Decplicado {decplicar(2)}')