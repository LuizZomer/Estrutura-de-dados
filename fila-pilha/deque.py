import numpy as np 

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.quantidade = 0
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1
    
    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print("Deque cheio")
            return 
        
        #Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
