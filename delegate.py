

def eh_par(number) :
    return number % 2 == 0

def eh_impar(number) :
    return number % 2 == 1

def imprima(e):
    print(e)

def imprime_lista(lst, imprima, condicao) :
    for e in lst :
        if condicao(e) :
            imprima(e)
        
if __name__ == '__main__' :
    lista = range(1,100)

    imprime_lista(lista, imprima, eh_par)
    imprime_lista(lista, imprima, eh_impar)