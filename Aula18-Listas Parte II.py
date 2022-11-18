# pessoa = []
# pessoa.append('Gustavo')
# pessoa.append(40)
# galera = []
# galera.append(pessoa[:])
# pessoa[0] = 'Maria'
# pessoa[1] = 22
# galera.append(pessoa[:])
# print(galera)
# for p in galera:
#     print(f'{p[0]}, {p[1]}')
galera = []
dados = []
for c in range(0, 2):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
