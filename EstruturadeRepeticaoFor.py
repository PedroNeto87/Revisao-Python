inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for i in range(inicio, fim, passo):
    print(i)
print('Fim')

print('_' * 30)

num = int(input('Informe um número de iterações? '))
soma = 0
for c in range(0, num):
    n = int(input('Informe um valor: '))
    soma += n
print(f'O somatorio dos valores informados foi de {soma}')
