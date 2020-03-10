import time

def geraNomes():
    """
    Essa função armazena uma sequência de nomes em uma lista e retorna uma lista de nomes de funcionários, cada um pertencente a uma empresa, e uma lista de empresas
    """
    l1 = []
    l2 = []
    k = 1
    print("""
    Você deve adicionar o nome de um funcionário por vez.

    No campo seguinte, digite o nome do domínio da empresa em que ele(a) trabalha (equivale ao nome que vem após o @ no email).

    Ao término, digite 0 no campo 'Nome do domínio da empresa'
    """)
    print()
    print()
    y = input("Domínio da empresa nº{}: ".format(k))
    x = input("Nome do funcionário: ")
    l1.append(y)
    l2.append(x)
    k += 1
    print()
    print()
    while y != 0:
        y = input("Domínio da empresa nº{}: ".format(k))
        if y == "0":
            break
        else:
            l1.append(y)
            x = input("Nome do funcionário: ")
            l2.append(x)
            k += 1
        print()

    return l1, l2


def geraPadroes(nomes, dominios):
    """
    Essa função recebe uma lista de nomes com sua lista de empresas correspondentes e gera uma lista com série de padrões de email possíveis
    """
    ListaDePadroes = []
    for i in range(0, len(dominios)):
        ListaDePadroes.extend(fazPadrao(nomes[i], dominios[i]))

    return ListaDePadroes


def fazPadrao(nome, dominio):
    padroes = []
    i = nome.split()

    p1 = i[0] + "_" + i[-1] + "@" + dominio
    p2 = i[0]+"." + i[-1] + "@" + dominio
    p3 = i[0] + "@" + dominio
    p4 = i[-1] + "@" + dominio
    p5 = i[0][0] + i[-1] + "@" + dominio
    p6 = i[0] + i[-1][0] + "@" + dominio
    p7 = i[0] + i[-1] + "@" + dominio
    p8 = i[-1][0] + "@" + dominio
    p9 = i[-1] + "." + i[0] + "@" + dominio
    p10 = i[-1] + "_" + i[0] + "@" + dominio
    p11 = i[0] + "-" + i[-1] + "@" + dominio
    p12 = i[0][0] + "-" + i[-1] + "@" + dominio
    p13 = i[0] + "-" + i[-1][0] + "@" + dominio
    p14 = i[0][0] + "_" + i[-1] + "@" + dominio
    p15 = i[0] + "." + i[-1][0] + "@" + dominio
    p16 = i[0] + "_" + i[-1][0] + "@" + dominio
    padroes.append(p1)
    padroes.append(p2)
    padroes.append(p3)
    padroes.append(p4)
    padroes.append(p5)
    padroes.append(p6)
    padroes.append(p7)
    padroes.append(p8)
    padroes.append(p9)
    padroes.append(p10)
    padroes.append(p11)
    padroes.append(p12)
    padroes.append(p13)
    padroes.append(p14)
    padroes.append(p15)
    padroes.append(p16)

    return padroes


def geraOutput(emails, numeroDeLinhas):
    """
    Essa função gera um output em .txt com a série de padrões de email possíveis
    """
    dia = time.asctime().split()
    data = "{}-{}".format(dia[2], dia[1])

    modo = open(r"PadroesEmail {}.txt".format(data), "w")
    for i in range(0, numeroDeLinhas - 1):
        modo.writelines("{}\n".format(emails[i]))
    modo.close()

    print()
    print("*")
    print("**")
    print("***")
    print("""
    Processo finalizado! =)
    ~> PadroesEmail (data).txt
    """)


def main():
    """
    Essa é a função principal do programa que consiste em gerar uma lista de padrões de email pré-definidos a partir de um input em arquivo txt contendo lista de nomes
    """
    ListaDeNomes = []
    ListaDeEmpresas = []
    input = geraNomes()
    ListaDeNomes.extend(input[1])
    ListaDeEmpresas.extend(input[0])

    padroes = geraPadroes(ListaDeNomes, ListaDeEmpresas)

    geraOutput(padroes, len(padroes))


main()