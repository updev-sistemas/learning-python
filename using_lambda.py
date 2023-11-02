
calcula_imposto = lambda value, tax : value * (tax/100)
calcula_desconto_salario = lambda value, discount : value - discount

if __name__ == '__main__' :
    salary = 1000.00
    inss = 17

    tax_value = calcula_imposto(salary, inss)
    salary_final = calcula_desconto_salario(salary, tax_value)
    print(salary_final)