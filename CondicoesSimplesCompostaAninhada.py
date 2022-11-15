tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
elif 3 < tempo <= 5:
    print('Carro semi-novo')
else:
    print('Carro velho')
print('--FIM--')