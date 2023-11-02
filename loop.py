
if __name__ == '__main__' :
    number = 1

    while (True):
        if number > 10000 and (number % 3 == 0 and number % 7 == 0 and number % 9 == 0):
            break
        number = number + 1
    
    print(number)