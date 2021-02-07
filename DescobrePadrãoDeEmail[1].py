import time

def fazPadrao(nome, dominio):
    if nome == "":
        return ""
    else:
        padroes = []
        i = nome.split()

        p1 = i[0] + i[-1] + "@" + dominio + "\n"
        p2 = i[0] + "_" + i[-1] + "@" + dominio + "\n"
        p3 = i[0]+"." + i[-1] + "@" + dominio + "\n"
        p4 = i[0] + "." + i[-1][0] + "@" + dominio + "\n"
        p5 = i[0] + i[-1][0] + "@" + dominio + "\n"
        p6 = i[0] + "@" + dominio + "\n"
        p7 = i[0] + "_" + i[-1][0] + "@" + dominio + "\n"
        p8 = i[0] + "-" + i[-1] + "@" + dominio + "\n"
        p9 = i[0] + "-" + i[-1][0] + "@" + dominio + "\n"
        p10 = i[0] + "_" + i[-1] + "@" + dominio + "\n"
        p11 = i[0][0] + "-" + i[-1] + "@" + dominio + "\n"
        p12 = i[0][0] + i[-1] + "@" + dominio + "\n"
        p13 = i[0][0] + "." + i[-1] + "@" + dominio + "\n"
        p14 = i[0][0] + "_" + i[-1] + "@" + dominio + "\n"
        p15 = i[-1] + dominio + "\n"
        p16 = i[-1] + i[0] + dominio + "\n"
        p17 = i[-1] + "." + i[0] + "@" + dominio + "\n"
        p18 = i[-1] + "_" + i[0] + "@" + dominio + "\n"
        p19 = i[-1] + i[0][0] + "@" + dominio + "\n"
        p20 = i[-1][0] + "@" + dominio + "\n"


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
        padroes.append(p17)
        padroes.append(p18)
        padroes.append(p19)
        padroes.append(p20)

        return padroes


def geraOutput(emails):
    """
    Essa função recebe uma lista de emails e gera um output em .txt com a série de padrões de email possíveis
    """
    dia = time.asctime().split()
    data = "{}-{}".format(dia[2], dia[1])
    with open(r"C:\Users\Lorenzo\Desktop\Padrões Possíveis {}.txt".format(data), "w", encoding = "UTF-8") as arq:
        for i in emails:
            arq.write(i)
        arq.close()

def padronizaNome(name):
    #PS: strings são imutáveis, portanto é preciso criar uma nova string
    name = name.lower().split("\n")[0]
    nova = ""
    for letra in name:
        if not "a" <= letra <= "z":
            if letra in ["ã", "á", "à", "â", "ä"]:
                nova += "a"
            elif letra in ["é", "è", "ê", "ë"]:
                nova += "e"
            elif letra in ["í", "ì", "î", "ï"]:
                nova += "i"
            elif letra in ["õ", "ó", "ò", "ô", "ö"]:
                nova += "o"
            elif letra in ["ú", "ù", "û", "ü"]:
                nova += "u"
            elif letra in ["ç"]:
                nova += "c"
            else:
                nova += letra
        else:
            nova += letra
    return nova



def main():
    """
    Essa é a função principal do programa que consiste em gerar uma lista de padrões de email pré-selecionados a partir de uma outra lista de nomes
    """
    Dominio = input("Domínio da empresa: ")
    ListaDeNomes, ListaDeEmails = [], []
    with open(r"C:\Users\Lorenzo\Desktop\Nomes.txt", "r", encoding = "utf-8") as arq:
        ListaDeNomes = arq.readlines()
        arq.close()
    for i in ListaDeNomes:
        i = padronizaNome(i)
        ListaDeEmails.extend(fazPadrao(i, Dominio))
    geraOutput(ListaDeEmails)


main()
