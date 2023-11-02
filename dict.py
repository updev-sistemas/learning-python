
if __name__ == '__main__' :

    dictionary = {
        "Width" : 14.2,
        "Height" : 13.2,
        "Size" : 23.2,
        "Weight" : 23.2
    }

    print("%10s %10s %10s %10s" % ('Width', 'Height', 'Size', 'Weight'))
    print("%10.2f %10.2f %10.2f %10.2f" % (dictionary['Width'], dictionary['Height'], dictionary['Size'], dictionary['Weight']))