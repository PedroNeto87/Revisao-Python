par = impar = somapar = somaimpar = somatot = 0
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
        somapar += n
    else:
        impar += 1
        somaimpar += n
    r = input('Quer continuar [S/N]? ').upper()
    if r == 'N':
        break
somatot = somapar + somaimpar
print(f'Você digitou {par} número(s) par(es) e {impar} número(s) impar(es)!')
print(f'A soma do(s) número(s) par(es) foi {somapar} e do(s) impar(es) foi {somaimpar}')
print(f'O somatorio total dos valores digitados foi {somatot}')
