import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    
    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False
        oi
        oi
    def __pilha_vazia(self):oi
        if self.__topo == -1:oi
            return True oi
        else:oi
            return Falseoi
        oi
        oi
    def empilhar(self, valor):oi
        oi
        if self.__pilha_cheia():oi
            print("Pilha cheia")oi

        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    
    def desempilhar(self):
        if self.__pilha_vazia():
            print("Pilha vazia")
        
        else:
            self.__topo -= 1
        
    
    def mostrar_topo(self):
        if not self.__pilha_vazia():
            print(self.__valores[self.__topo])


p1 = Pilha(5)
p1.empilhar(1)
p1.empilhar(3)
p1.mostrar_topo()
p1.empilhar(5)
p1.mostrar_topo()
p1.desempilhar()
p1.mostrar_topo()
p1.desempilhar()
p1.mostrar_topo()
p1.desempilhar()
p1.mostrar_topo()
p1.desempilhar()
p1.mostrar_topo()

        
