import os
if __name__ == '__main__' :

    # print(os.cpu_count())
    # print(os.environ)
    # print(os.getenv("VSCODE_GIT_ASKPASS_MAIN"))

    arquivo = open('C:\Workspace\\test_escrita.txt', 'a')

    for linha in range(100) :
        arquivo.write("Incluindo a linha %d ao arquivo\n" % (1 + linha))

    arquivo.close()

    arquivo = open('C:\Workspace\\test_escrita.txt', 'r')

    for linha in arquivo.readlines() :
        print(linha)

    arquivo.close()