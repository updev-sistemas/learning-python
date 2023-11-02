import random

if __name__ == '__main__' :
    list = []

    for i in range(10) :
        list.append(random.randint(1, 1000))

    print(list)
    
    random.shuffle(list)
    print(list)