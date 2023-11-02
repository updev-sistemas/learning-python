
def sum(*arg) :
    _sum = 0
    for n in arg :
        try :
            value = float(n)
            _sum += value
        except:
            _sum += 0
    return _sum

def minus(number_a, number_b) :
    return number_a - number_b