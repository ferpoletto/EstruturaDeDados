class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

    def mostrar(self):
        return print(f'{self.dados}')

pilha = Pilha()

pilha.empilha(1)
pilha.empilha(60)
pilha.mostrar()
pilha.desempilha()
pilha.mostrar()

