

def dequeue(vector) -> int:
    result = vector.pop()
    return result

def enqueue(vector, number):
    vector.append(number)

def new_number() -> int :
    result = int(input('Digite o numero: '))
    return result

if __name__ == '__main__' :
    vector = list()

    while (True) :
        print('Digite 1 para enfileirar')
        print('Digite 2 para desenfileirar ')
        print('Digite 0 para sair. ')
        inpt = int(input('Digite a opcao '))

        if inpt == 0 :
            break
        elif inpt == 1 :
            enqueue(vector, new_number())
        elif inpt == 2 :
            number = dequeue(vector)
            print('Proximo da fila: %d.' % number)
        else :
            print ('Opcao invalida, tente novamente.')
    
        print(vector)
