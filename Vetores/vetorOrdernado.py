import numpy as np

class VetorOrdenado:

    def  __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)


    def __vetor_cheio(self):
        return self.ultima_posicao == self.capacidade - 1
    

    def __vetor_vazio(self):
        return self.ultima_posicao == -1

    
    def adicionar(self, valor):
        if self.__vetor_cheio():
            print("Vetor cheio")

        else:
            posicao = 0
            for i in range(self.ultima_posicao + 1):
                posicao = i
                if self.valores[i] > valor:
                    break

                if i == self.ultima_posicao:
                    posicao = i + 1

            x = self.ultima_posicao

            while x >= posicao:
                self.valores[x + 1] = self.valores[x]
                x -= 1
            
            self.valores[posicao] = valor
            self.ultima_posicao += 1


    def mostrar(self):
        if self.__vetor_vazio():
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])

    
    def pesquisa_binaria(self, valor):
        inicio = 0
        fim = self.ultima_posicao
        
        while True:
            posicao_atual = (inicio + fim)//2
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif inicio == fim:
                return -1
            else:
                if self.valores[posicao_atual] > valor:
                    fim = posicao_atual - 1
                else:
                    inicio = posicao_atual + 1
    
    def excluir(self, valor):
        if self.__vetor_vazio():
            print("Vetor vazio")
    
        else:
            posicao = self.pesquisa_binaria(valor)

            if posicao == -1:
                return -1
            else:
                for i in range(posicao, self.ultima_posicao):
                    self.valores[i] = self.valores[i + 1]
                self.ultima_posicao -= 1


v1 = VetorOrdenado(6)
v1.adicionar(89)
v1.adicionar(10)
v1.adicionar(4)
v1.adicionar(48)
v1.adicionar(1)
v1.adicionar(-3)
# v1.adicionar(100)
v1.mostrar()
# print(v1.pesquisa_binaria(89))
v1.excluir(-3)
v1.mostrar()