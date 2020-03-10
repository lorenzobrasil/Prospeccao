import time
def main():
    """
    Essa é a função principal do programa, que irá retornar uma lista de emails com base em um input de nomes, em arquivo txt,um padrão especificado de email
    """
    padrao = int(input("""
  Escolha o número correspondente a um padrão de email:
  
  1- [nome]_[sobrenome]@dominio
  2- [nome].[sobrenome]@dominio
  3- [nome]@dominio
  4- [sobrenome]@dominio
  5- [n][sobrenome]@dominio
  6- [nome][s]@dominio
  7- [nome][sobrenome]@dominio
  8- [sobrenome][Nome]@dominio
  9- [sobrenome].[nome]@dominio
  10- [sobrenome]_[nome]@dominio
  11- [n].[sobrenome]@dominio
  12- [nome].[s]@dominio
  13- [N]_[sobrenome]@dominio
  14- [nome]_[s]@dominio
  15- [nome]-[sobrenome]@dominio
  16- [n]-[sobrenome]@dominio
  17- [nome]-[s]@dominio
  
  número: 
  """))
    dominio = input("Domínio do email: ")
    print()
    print()
    print("""
  Agora você deve criar um arquivo de texto com o título Nomes e salvar no bloco de notas (no formato txt)
  """)
    nomes = []
    nomes.extend(leNomes())

    dia = time.asctime().split()
    global data
    data = "{}-{}".format(dia[2], dia[1])
    geraOutput(nomes, dominio, padrao)



def geraOutput(nomes, dominio, padrao):
    arquivoFinal = open(r"C:\Users\Lorenzo\Desktop\Lista de Emails {}.txt".format(data), "w", encoding="utf-8")
    if padrao == 1:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao1(nomes[nome], dominio) + "\n")

    elif padrao == 2:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao2(nomes[nome], dominio) + "\n")

    #2 - nome.sobrenome @ dominio

    elif padrao == 3:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao3(nomes[nome], dominio) + "\n")

    #3 - nome @ dominio

    elif padrao == 4:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao4(nomes[nome], dominio) + "\n")

        #4 - sobrenome @ dominio

    elif padrao == 5:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao5(nomes[nome], dominio) + "\n")

        #5 - Nsobrenome @ dominio

    elif padrao == 6:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao6(nomes[nome], dominio) + "\n")

    #6 - nomes @ dominio

    elif padrao == 7:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao7(nomes[nome], dominio) + "\n")

    #7 - nomesobrenome @ dominio

    elif padrao == 8:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao8(nomes[nome], dominio) + "\n")

    #8 - sobrenomeNome @ dominio

    elif padrao == 9:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao9(nomes[nome], dominio) + "\n")

    #9 - sobrenome.nome @ dominio

    elif padrao == 10:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao10(nomes[nome], dominio) + "\n")

    #10 - sobrenome_nome @ dominio

    elif padrao == 11:
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao11(nomes[nome], dominio) + "\n")

    #11 - n.sobrenome @ dominio

    elif padrao == 12:
        # 12 - nome.s @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao12(nomes[nome], dominio) + "\n")


    elif padrao == 13:
        # 13 - N_sobrenome @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao13(nomes[nome], dominio) + "\n")

    elif padrao == 14:
        # 14 - nome_s @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao14(nomes[nome], dominio) + "\n")

    elif padrao == 15:
        #15 - [nome] - [sobrenome] @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao15(nomes[nome], dominio) + "\n")

    elif padrao == 16:
        #16 - [n] - [sobrenome] @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao16(nomes[nome], dominio) + "\n")
    elif padrao == 17:
        #17 - [nome] - [s] @ dominio
        for nome in range(0, len(nomes)):
            arquivoFinal.writelines(fazPadrao17(nomes[nome], dominio) + "\n")

    arquivoFinal.close()
    print("*")
    print("**")
    print("***")
    print("""
    Processo finalizado! =)
        
    Arquivo -> NomesFeitos.txt
    """)



def fazPadrao1(nome, dominio):
    name = nome.split()
    return name[0]+"_"+name[-1]+"@"+dominio

def fazPadrao2(nome, dominio):
    name = nome.split()
    return name[0]+"."+name[-1]+"@"+dominio

def fazPadrao3(nome, dominio):
    name = nome.split()
    return name[0]+"@"+dominio

def fazPadrao4(nome, dominio):
    name = nome.split()
    return name[-1]+"@"+dominio

def fazPadrao5(nome, dominio):
    name = nome.split()
    return name[0][0]+name[-1]+"@"+dominio

def fazPadrao6(nome, dominio):
    name = nome.split()
    return name[0]+name[-1][0]+"@"+dominio

def fazPadrao7(nome, dominio):
    name = nome.split()
    return name[0]+name[-1]+"@"+dominio

def fazPadrao8(nome, dominio):
    name = nome.split()
    return name[-1]+name[0]+"@"+dominio

def fazPadrao9(nome, dominio):
    name = nome.split()
    return name[-1]+"."+name[0]+"@"+dominio

def fazPadrao10(nome, dominio):
    name = nome.split()
    return name[-1]+"_"+name[0]+"@"+dominio

def fazPadrao11(nome, dominio):
    name = nome.split()
    return name[0][1]+"."+name[-1]+"@"+dominio

def fazPadrao12(nome, dominio):
    name = nome.split()
    return name[0]+"."+name[-1][0]+"@"+dominio

def fazPadrao13(nome, dominio):
    name = nome.split()
    return name[0][0]+"_"+name[-1]+"@"+dominio

def fazPadrao14(nome, dominio):
    name = nome.split()
    return name[0]+"_"+name[-1][0]+"@"+dominio

def fazPadrao15(nome, dominio):
    name = nome.split()
    return name[0] + "-" + name[-1] + "@" + dominio

def fazPadrao16(nome, dominio):
    name = nome.split()
    return name[0][0] + "-" + name[-1] + "@" + dominio

def fazPadrao17(nome, dominio):
    name = nome.split()
    return name[0] + "-" + name[-1][0] + "@" + dominio


def leNomes():
    """
    Lê os nomes contidos em um arquivo txt, remove os separadores (\n) e devolve uma lista em que cada elemento corresponde a um nome
    """
    nomes = []
    arquivo = open(r"C:\Users\Lorenzo\Desktop\Nomes.txt", "r", encoding="utf-8")
    for nome in arquivo:
        nomes.append(nome)
    arquivo.close()
    k = 0
    while k < (len(nomes)-1):
        nomes[k] = nomes[k][:(len(nomes[k])-1)]
        k+=1
    return nomes


main()