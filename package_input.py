if __name__ == '__main__' :
    try :
        print(1/0)
    except:
        raise ZeroDivisionError("Ocorreu um erro tosco")