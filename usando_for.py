
if __name__ == '__main__' :
    for t in range(0,100, 2) :
        print(t, end = " ")
    print()

    list_numbers = range(1,1000, 3)

    for value, key in enumerate(list_numbers) :
        print(value, key)