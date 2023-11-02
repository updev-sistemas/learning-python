if __name__ == '__main__' :
    nome = 'Aprendendo Python'

    inicia_com_ap = nome.lower().startswith('ap')

    if inicia_com_ap :
        print('Inicia com AP')
    else :
        print('Nao inicia com AP')

    termina_com_on = nome.lower().endswith('op')

    if termina_com_on :
        print('Termina com OP')
    else :
        print('Nao termina com OP')


    s = 'Antonio Carlos Barros'

    
    # contains_jose = 'jose' in s.lower()
    contains_jose = 'jose' not in s.lower()
    if contains_jose :
        print('Tem Jose em sua composicao')
    else :
        print('Nao tem Jose em sua composicao')


    s = 'Um tigre, dois tigres, tres tigres'
    count_tigre = s.lower().count('tigre')
    print('Temos %d tigre(s)' % count_tigre)
