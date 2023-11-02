import sys

if __name__ == '__main__' :
    
    if len(sys.argv) > 1 :
        file = open(sys.argv[1], 'r')

        for line in file.readlines() :
            print(line)
            
    else :
        print('Arquivo nao foi informado.')