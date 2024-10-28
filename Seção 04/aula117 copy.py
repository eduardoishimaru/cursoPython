import json
import os
os.system('cls')

# pessoas=[
#     {
#         "nome":'maria',
#         "sobrenome": 'vieira',
#         "idade": 25,
#         "notas": ['A','A+'],
#         "telefones": {
#             "residencial":"00 0000-0000",
#             "celular":"00 0000-0000"
#         }

#     },
#     {
#         "nome":'joana',
#         "sobrenome": 'teste',
#         "idade": 30,
#         "notas": ['A','B+'],
#         "telefones": {
#             "residencial":"00 0000-0000",
#             "celular":"00 0000-0000"
#         }

#     }

# ]




# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAVE_TO, 'w' , encoding='utf-8') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas,indent=2))



BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE,'r') as file:
    pessoas = json.load(file)
    #print(pessoas)

    # for pessoa in pessoas:
    #     print(pessoa['nome'])
