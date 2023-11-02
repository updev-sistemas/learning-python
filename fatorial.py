def fatorial(n):
    print("Calculando o fatorial de %d" % n)
    if n==0 or n == 1:
        print("Fatorial %d = 1" % n)
        return 1
    else:
        fat = n*fatorial(n-1)
        print(" fatorial %d = %d" % (n, fat) )
        return fat

if __name__ == '__main__' :
    print(fatorial(10))