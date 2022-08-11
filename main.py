# aluno: Leonardo Ikeda

'''
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá determinar se uma string de
entrada faz parte da linguagem 𝐿 definida por 𝐿 = {𝑥 | 𝑥 ∈ {𝑎, 𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏}
segundo o alfabeto Σ = {𝑎, 𝑏, 𝑐}.

O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha. A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
  
    3
    abbaba
    abababb
    bbabbaaab
    
Neste exemplo temos 3 strings de entrada. O número de strings em cada arquivo será
representado por um número inteiro positivo. A resposta do seu programa deverá conter uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
    
    abbaba: não pertence.
    
A saída poderá ser enviada para um arquivo de textos, ou para o terminal padrão e será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.

Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de
testes criado pelo próprio professor.
'''

# Dicionario de letras // Dictionary of letters
def dicionario(abc):
    def letras(a, *b, **c):
        x = abc(a, *b, **c)
        x.send(None)
        return x

    return letras


# Maquina de estados finitos // Finite state machine
class MaquinaDeEstadosFinitos:
    # Definindo os nodes, estado e fim // Defining nodes, state and end
    def __init__(self):

        self.node1 = self.inicianode1()
        self.node2 = self.inicianode2()
        self.node3 = self.inicianode3()
        self.node4 = self.inicianode4()
        self.node5 = self.inicianode5()
        self.estado = self.node1
        self.fim = False

    # Node de chegada // Arrival node
    def chegada(self):

        if self.estado == self.node4:
            return "Pertence"
        else:
            return "Não pertence"

    # Funcao de envio // Send function
    def send(self, letra):

        try:
            self.estado.send(letra)
        except:
            self.fim = True

    # Primeiro node e suas ações // First node and its actions
    @dicionario
    def inicianode1(self):

        while True:
            letra = yield

            if letra == "a":
                self.estado = self.node2

            elif letra == "b":
                self.estado = self.node5

            elif letra == "c":
                self.estado = self.node5

            else:
                break

    # Segundo node e suas ações // Second node and its actions
    @dicionario
    def inicianode2(self):

        while True:
            letra = yield

            if letra == "b":
                self.estado = self.node3

            else:
                break

    # Terceiro node e suas ações // Third node and its actions
    @dicionario
    def inicianode3(self):

        while True:
            letra = yield

            if letra == "b":
                self.estado = self.node4

            else:
                break

    # Quarto node e suas ações // Fourth node and its actions
    @dicionario
    def inicianode4(self):

        while True:
            letra = yield

            if letra == "b":
                self.estado = self.node4

            elif letra == "c":
                self.estado = self.node4

            elif letra == "a":
                self.estado = self.node2

            else:
                break

    # Quinto node e suas ações // Fifth node and its actions
    @dicionario
    def inicianode5(self):

        while True:
            letra = yield

            if letra == "b":
                self.estado = self.node5

            elif letra == "c":
                self.estado = self.node5

            elif letra == "a":
                self.estado = self.node2

            else:
                break


# Envia as leituras para o send e verifica a chegada // Send readings to send and check arrival
def arquivo(self):
    Maquina = MaquinaDeEstadosFinitos()
    for letra in self:
        Maquina.send(letra)
    return Maquina.chegada()


def main():
    # Cria uma lista e abre o arquivo txt e ler as linhas // Create a list and open the txt file and read the lines
    listadeletras1 = []
    with open("Lista1.txt") as lista1:
        for int, line in enumerate(lista1):
            int, listadeletras1.append(line.strip())

    # inicia um loop para mostrar os resultados // start a loop to show the results
    for i in listadeletras1[1:]:
        print(i.rstrip('\n'), arquivo(i), sep=": ")

    print("----------")

    listadeletras2 = []
    with open("Lista2.txt") as lista2:
        for int, linha in enumerate(lista2):
            int, listadeletras2.append(linha.strip())

    for i in listadeletras2[1:]:
        print(i.rstrip('\n'), arquivo(i), sep=": ")

    print("----------")

    listadeletras3 = []
    with open("Lista3.txt") as lista3:
        for int, linha in enumerate(lista3):
            int, listadeletras3.append(linha.strip())

    for i in listadeletras3[1:]:
        print(i.rstrip('\n'), arquivo(i), sep=": ")


if __name__ == "__main__":
    main()
