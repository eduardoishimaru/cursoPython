import os
os.system('cls')


caminho_arquivo = r'C:\\Users\\Eduardo\\Documents\\GitHub\\cursoPython\\'
caminho_arquivo += 'aula116.txt'

# arquivo =open(caminho_arquivo,'w')
# #
# arquivo.close()

with open(caminho_arquivo,'w+', encoding='utf-8') as arquivo:
    print(type(arquivo))
    print('Olá mundo')
    print('Arquivo vai ser fechado')
    arquivo.write('Linha 1 ação\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n','Linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    
    print('#'*100)
    print('Lendo')
    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')

    print('#'*100)

    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())



print('#'*100)

with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.read())


##Apagar o arquivo
#os.remove(caminho_arquivo)

#renomeia ou move o arquivo
#os.rename(caminho_arquivo, 'aula116-old.txt')
