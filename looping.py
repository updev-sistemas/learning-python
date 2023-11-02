
if __name__ == '__main__' :
    inicio = 0
    final = 100

    while inicio <= final :
        if inicio % 2 == 0 :
            print('Numero %d e par.' % inicio)
        else :
            print('Numero %d e impar.' % inicio)
        inicio = inicio + 1