import numpy as np

class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)


    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor cheio")
        
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor


    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i])

    
    def apagar(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == -1:
            return -1
        
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]

        self.ultima_posicao -= 1


    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
            
        return -1


v1 = VetorNaoOrdenado(3)

v1.inserir(1)
v1.inserir(56)
v1.inserir(3)

# print(v1.pesquisar(1))
v1.apagar(3)

v1.inserir(6)

v1.imprimir()
