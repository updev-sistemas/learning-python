
def calcular(qtd, preco_unitario, desconto = 0) :
    total = (qtd * preco_unitario)
    desconto_total = total * (desconto / 100)

    return total - desconto_total

if __name__ == '__main__' :
    
    print(calcular(2, 4.3, 10))
    print(calcular(2, 4.3))
    print(calcular(2, 4.3, 11))
    print(calcular(2, 4.3))
    print(calcular(2, 4.3, 4))