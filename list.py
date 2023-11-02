
def sum_vector(vect) -> float :
    sum = 0
    for n in vect :
        sum += n
    return sum

def avg_vector(vect) -> float :
    sum = sum_vector(vect)
    return sum / len(vect)

def print_result(vector, avg) :
    print(vector)
    print('Avarage %f.' % avg)

if __name__ == '__main__' :
    l = [0,1,2,3,4,5,6,7,8,9]

    avg = avg_vector(l)
    print_result(l, avg)

    l.append(3)
    avg = avg_vector(l)
    print_result(l, avg)

    l += [3,3,5,6]
    avg = avg_vector(l)
    print_result(l, avg)

    l.extend([3,4,5])
    avg = avg_vector(l)
    print_result(l, avg)

    del l[:-3]
    avg = avg_vector(l)
    print_result(l, avg)

    l = list(range(100))
    avg = avg_vector(l)
    print_result(l, avg)