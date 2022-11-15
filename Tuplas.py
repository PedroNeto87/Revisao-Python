lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
for i in lanche:
    print(i, end=' ')
print()
for cont in range(0, len(lanche)):
    print(cont, lanche[cont], end=' ')
print()
for pos, comida in enumerate(lanche):
    print(pos, comida, end=' ')
