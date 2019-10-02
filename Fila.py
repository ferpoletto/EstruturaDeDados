class Fila(object):
    def __init__(self):
        self.dados = []

    def insere(self, elemento):
        self.dados.append(elemento)

    def retira(self):
        return self.dados.pop(0)

    def vazia(self):
        return len(self.dados) == 0

    def mostrar(self):
        return print(f'{self.dados}')

fila = Fila()

fila.insere(28)
fila.mostrar()
fila.insere(42)
fila.mostrar()
fila.insere(46)
fila.mostrar()
fila.retira()
fila.mostrar()
fila.retira()
fila.mostrar()
fila.insere(200)
fila.mostrar()

