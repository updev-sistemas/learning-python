if __name__ == '__main__' :
    print('-- AND --------')
    print(True and True)
    print(True and False)
    print(False and True)
    print(False and False)
    print('---------------')

    print('-- OR --------')
    print(True or True)
    print(True or False)
    print(False or True)
    print(False or False)
    print('--------------')

    print('-- NOT --------')
    print(not True)
    print(not False)
    print('---------------')

    print('-- SE ENTAO --------')
    print(not True or True)
    print(not True or False)
    print(not False or True)
    print(not False or False)
    print('--------------------')


    str = 'Antonio Jose'
    print(str)
    print(len(str))
    print(str[0])

    print('A' * 10)
    print('VAMOS\n' * 3 + '\n' + 'TIMAO\n' * 2)

    print('Ola %s, voce tem %d anos de idade e um saldo bancario de %03d.' % ('Antonio Jose', 34, -2450))

    #        1.003.333
    salary = 1333.4543
    print("Salario %10.2f" % salary)

    print(len('---------------------------------------------------------'))

    print('---- Holerite ----------------------------------------------')
    print('Nome: %54s' % 'Antonio Jose')
    print('Matricula: %49d' % 4342)
    print('Salario: %51.2f' % 8549.142)
    print('------------------------------------------------------------')

    letra = 'Ainda, que eu falasse a lingua dos homens, sem amor, eu nada seria.'
    letra_len = len(letra)
    print(letra_len)
    search_word = 'falasse'
    len_word = len(search_word)
    position = letra.index(search_word)

    print(letra[position : position + len_word])

    print(letra[:])
    print(letra[:0])
    print(letra[0:letra_len])
    print(letra[5:11])
    print(letra[-5:-11])
