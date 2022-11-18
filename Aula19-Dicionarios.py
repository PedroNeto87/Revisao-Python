# dados1 = {'nome': 'Pedro', 'idade': 35}
# print(dados1['nome'])
# print(dados1['idade'])
# dados1['sexo'] = 'M'
# print(f'O {dados1["nome"]} tem {dados1["idade"]} anos')
# del dados1['idade']
# print(dados1)
# print(dados1.values())
# print(dados1.keys())
# print(dados1.items())
#
# print('-=' * 10)
# for k, v in dados1.items():
#     print(f'{k}: {v}')
#
# print('-=' * 10)
# dados2 = {'nome': 'Ashia', 'idade': 30}
# clientes = list()
# clientes.append(dados1)
# clientes.append(dados2)
# print(clientes[0]['nome'])
estado = {}
brasil = []

for c in range(0,2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())#Importante: Dicionário tem método próprio para copiar uma lista.
for e in brasil:#laço para uma lista
    for v in e.values():#laço para um dicionário
        print(v, end=' ')
    print()
