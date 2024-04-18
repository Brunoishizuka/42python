class Elemento:
    def __init__(self, element, position, number, small, molar, electron):
        self.elemento = element
        self.posicao = position
        self.numero = number
        self.sigla = small
        self.mol = molar
        self.eletron = electron


def ler_arquivo():
    tabela = open('periodic_table.txt', 'r')
    table = tabela.read().split("\n")
    tabela.close()  # Close the file after reading
    return table


def ler_tabela():
    dadostabela = ler_arquivo()

    lista_elementos = list()

    for var in dadostabela:
        if var:
            dadoselemento = var.split(',')
            nomeelemento = dadoselemento[0].split('=')
            posicaoelemento = nomeelemento[1].split(':')
            numeroelemento = dadoselemento[1].split(':')
            siglaelemento = dadoselemento[2].split(':')
            molelemento = dadoselemento[3].split(':')
            eletronelemento = dadoselemento[4].split(':')

            element = Elemento(nomeelemento[0], posicaoelemento[1], numeroelemento[1], siglaelemento[1],
                               molelemento[1], eletronelemento[1])

            lista_elementos.append(element)

    tabela = ""
    anterior = 0

    for obj in lista_elementos:
        contador = 0
        if int(anterior) < 18:
            contador = int(anterior)
        if contador == 0:
            abretr = "<tr>"
            tabela = tabela + abretr
        while contador < 18:
            if contador == int(obj.posicao):
                inserirlinha = "<td style=\"border: 2px solid black; padding:10px\"><h4>" + obj.elemento + "</h4></ul><li>No " + obj.numero + "</li><li>" + obj.sigla + "</li><li>" + obj.mol + "</li><li>" + obj.eletron + " electron</li></ul></td>"
                tabela = tabela + inserirlinha
                anterior = int(obj.posicao) + 1
                if contador == 17:
                    fechatr = "</tr>"
                    tabela = tabela + fechatr
                break
            else:
                abrefechatd = "<td border-style: none></td>"
                tabela = tabela + abrefechatd
            contador = contador + 1

    pagina_html(tabela)


def pagina_html(tabela):
    with open("periodic_table.html", "w") as html:
        html.write("<!DOCTYPE html>\n")
        html.write("<html>\n")
        html.write("<head>\n")
        html.write("<title>Periodic Table</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write("<table>\n")
        html.write(tabela)
        html.write("</table>\n")
        html.write("</body>\n")
        html.write("</html>\n")


if __name__ == "__main__":
    ler_tabela()
