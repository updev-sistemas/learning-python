if __name__ == '__main__' :
    text = 'O método split quebra uma string a partir de um caractere passado como parâmetro, retornando uma lista com as substrings já separadas'

    text = text.replace(',', '')
    arr = text.split(' ')
    
    print(arr)


    text = '        ANTONIO JOSE         '

    print(text)
    print(text.strip())

    str = ''

    if not str.isalnum() :
        print('String vazia ou nula.')

    str = 'Antonio Jose 123'

    if not str.isalpha() :
        print('String com alfabeto.')