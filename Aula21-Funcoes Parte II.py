def somar(a=0, b=0, c=0): #Função com paramentros opcionais
    #docstrings
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    """
    s = a + b + c
    print(f'A soma vale {s}')


def teste(b):
    global a #torna a variável local uma variável global
    a = 8 #escopo local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C Dentro vale {c}')


def soma(a=0, b=0, c=0): #função com retorno
    s = a + b + c
    return s


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
somar(2, 3)
a = 5 #escopo global
teste(a)
print(f'A fora vale {a}')
r1 = soma(3, 2, 5)
print(f'A soma vale {r1}')
