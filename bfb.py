def verify(str) -> bool :
    stack = []

    for c in str :
        if c == '(' :
            stack.append(c)
        elif c == ')' :
            stack.pop(-1)
        elif c == '[' :
            stack.append(c)
        elif c == ']' :
            stack.pop(-1)
        elif c == '{' :
            stack.append(c)
        elif c == '}' :
            stack.pop(-1)

    return len(stack) == 0

if __name__ == '__main__' :
    str_to_verify = input('Digite o Padrao: ')

    if len(str_to_verify) == 0 :
        print('Padrao Invalido.')
    else :
        result = verify(str_to_verify)
        if result :
            print('Padrao [%s] e valida' % str_to_verify)
        else :
            print('Padrao [%s] e invalida' % str_to_verify)