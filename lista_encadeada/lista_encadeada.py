import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
    def mostrar_no(self):
        print(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo


lista = ListaEncadeada()
lista.inserir_inicio(1)
lista.inserir_inicio(3)
lista.primeiro
lista.mostrar()