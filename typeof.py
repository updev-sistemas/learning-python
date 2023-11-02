
if __name__ == '__main__' :

    def i() :
        print('Teste')

    class Person(object) :
        def __init__(self) -> None:
            pass

    a = 1
    b = 2.3
    c = 'c'
    d = "Vamos ver"
    e = True
    f = []
    g = {}
    h = lambda x : x * 2
    j = Person()


    print(type(a)) # <class 'int'>
    print(type(b)) # <class 'float'>
    print(type(c)) # <class 'float'>
    print(type(d)) # <class 'str'>
    print(type(e)) # <class 'bool'>
    print(type(f)) # <class 'list'>
    print(type(g)) # <class 'dict'>
    print(type(h)) # <class 'function'>
    print(type(i)) # <class 'function'>
    print(type(j)) # <class 'function'>