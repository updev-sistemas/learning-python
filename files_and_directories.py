import os 

if __name__ == '__main__' :
    path = os.getcwd() # raiz do aplicativo
    print(path)

    os.mkdir('Test_Dir', 655)
    os.chdir('Test_Dir')
    os.mkdir('Test_Dir_A', 655)
    os.chdir('Test_Dir_A')
    os.mkdir('Test_Dir_A_Internal_A', 655)
    os.mkdir('Test_Dir_A_Internal_B', 655)

    os.makedirs('Music/Rock/Janeiro')
    os.makedirs('Music/Rock/Fevereiro')
    os.makedirs('Music/Rock/Marco')

    os.chdir('../../../../')
    os.rename('Teste', 'Teste_Renomeado')