

def calcular(qtd, preco_unitario, desconto = 0) :
    total = (qtd * preco_unitario)
    desconto_total = total * (desconto / 100)

    return total - desconto_total

if __name__ == '__main__' :
    
    print(calcular(desconto= 10, qtd = 2, preco_unitario= 3.40))
    print(calcular(qtd = 2, desconto= 10, preco_unitario= 3.40))