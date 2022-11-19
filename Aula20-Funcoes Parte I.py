def soma(a, b): #função do passagem de parametro.
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma vale {s}')


def contador(* núm):
    tam = len(núm)
    for valor in núm:
        print(valor, end=' ')
    print()
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def nova_soma(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f'A soma dos valores {numeros} foi {s}')


soma(4, 5)
contador(2, 3, 5, 7)
valores = [7, 2, 5, 0, 2]
print(f'Lista antes da função dobra: {valores}')
dobra(valores)
print(f'Lista depois da função dobra: {valores}')
nova_soma(2, 3, 9, 15)
nova_soma(9, 12, 1)
