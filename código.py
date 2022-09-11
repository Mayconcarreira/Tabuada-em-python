valor = int(input('Digite um valor para saber a tabuada :  '))
aux = 0

print('-' * 19)
print('   Tabuda de {}'.format(valor))
print('-' * 19)

while (aux <= 10):
    print ('{0} x {1} = {2}'.format(aux, valor, (aux * valor)))
    aux += 1
