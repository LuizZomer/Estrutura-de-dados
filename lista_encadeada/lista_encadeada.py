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
        if self.primeiro == None:
            print("A lista está vazia")
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo


    def pesquisa(self, valor):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
        
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            atual = atual.proximo
        return atual

    
    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print("A lista está vazia")
            return None
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            anterior = atual
            atual = atual.proximo
        if atual == self.primeiro:
            self.excluir_inicio()
        else:
            anterior.proximo = atual.proximo
        
        return atual


lista = ListaEncadeada()
lista.inserir_inicio(1)
lista.inserir_inicio(2)
lista.inserir_inicio(3)
lista.inserir_inicio(4)
# lista.mostrar()
# lista.excluir_inicio()
# lista.excluir_inicio()
# lista.mostrar()
# pesquisa = lista.pesquisa(3)
lista.excluir_posicao(2)
lista.mostrar()

# if pesquisa != None:
#     print(f"Valor encotrado: {pesquisa.valor}")

# else:
#     print('Valor não encontrado')