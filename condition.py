tarifa_residencial_ate_500 = 0.40
tarifa_residencial_acima_500 = 0.65
tarifa_comercial_ate_1000 = 0.55
tarifa_comercial_acima_1000 = 0.60
tarifa_industrial_ate_5000 = 0.55
tarifa_industrial_acima_5000 = 0.60

def calcula_conta_luz( consumo, tarifa) :
    return consumo * tarifa

def selecione_tarifa( consumo ):
    if (consumo > 5000)  :
        return tarifa_industrial_acima_5000
    elif (consumo > 1000 and consumo <= 5000) :
        return tarifa_industrial_ate_5000 
    elif (consumo > 1000) :
        return tarifa_comercial_acima_1000
    elif (consumo > 500 and consumo <= 1000) :
        return tarifa_comercial_ate_1000
    elif (consumo > 500):
        return tarifa_residencial_acima_500
    elif (consumo <= 500):
        return tarifa_residencial_ate_500
    else :
        raise Exception('Leitura invalida.')

if __name__ == '__main__' :
    consumo_digitado = input('Digite o consumo: ')

    try :
        consumo_convertido = float(consumo_digitado)

        tarifa_selecionada = selecione_tarifa(consumo_convertido)

        valor_a_ser_pago = calcula_conta_luz(consumo_convertido, tarifa_selecionada)

        print("Sua conta e de R$ %.2f." % valor_a_ser_pago)

    except :
        print('Entrada invalida.')

