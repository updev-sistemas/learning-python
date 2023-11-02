
def somar(a, b) :
    return a + b

def subtrair(a, b) :
    return a - b

def multiplicar(a, b) :
    return a * b

def dividir(a, b) :
    return a / b

def imprimir_resultado(a, b, func) :
    print(func(a, b))

if __name__ == '__main__' :
    imprimir_resultado(20, 2, somar)
    imprimir_resultado(20, 2, subtrair)
    imprimir_resultado(20, 2, multiplicar)
    imprimir_resultado(20, 2, dividir)