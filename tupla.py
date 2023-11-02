
if __name__ == '__main__' :
    tuplas = [
        (1, 'Antonio Jose', 'antoniojose@live.com', 1.75, 109),
        (2, 'Paulo Vitor', 'paulovitor@live.com', 1.74, 110),
        (3, 'Naiara', 'naiara@live.com', 1.65, 75)
    ]

    print("%-5s %-20s %-30s %-8s %-8s" % ('ID', 'Nome', 'Email', 'Altura', 'Peso'))
    for tupla in tuplas :
        print("%-5s %-20s %-30s %-8s %-8s" % tupla)