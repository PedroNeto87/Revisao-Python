num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
num.pop()
print(num)
valores = []
for c in range(0,5):
    valores.append(int(input('Informe um valor: ')))

for i, v in enumerate(valores):
    print(f'Na posição {i+1} encontrei o valor {v}')
print(f'Numero de elementos: {len(valores)}')

b = valores[:]
b[2] = 100
print(f'Lista A: {valores}')
print(f'Lista B: {b}')
