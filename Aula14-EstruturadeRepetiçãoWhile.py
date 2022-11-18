c = 1
while c != 10:
    print(c)
    c += 1
print('Acabou')
par = impar = somapar = somaimpar = somatot = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
        somapar += n
    else:
        impar += 1
        somaimpar += n
    r = input('Quer continuar [S/N]? ').upper()
somatot = somapar + somaimpar
print(f'Você digitou {par} número(s) par(es) e {impar} número(s) impar(es)!')
print(f'A soma do(s) número(s) par(es) foi {somapar} e do(s) impar(es) foi {somaimpar}')
print(f'O somatorio total dos valores digitados foi {somatot}')
