class Produto:
    def __init__(self, cod, pre, qtd):
        self.codigo = cod
        self.preco = pre
        self.quantidade = qtd
    def mostrar(self):
        print(f"Codigo: {self.codigo}\tPreço: {self.preco}\tQuantidade: {self.quantidade}")


class Node:
    produto = None
    prox = None


class Lista:
    tamanho = 0
    topo = None

    def add(self, newProduto):
        aux = Node()
        aux.produto = newProduto
        self.tamanho += 1
        if self.topo == None:
            self.topo = aux
        else:
            aux.prox = self.topo
            self.topo = aux

    def excluir(self):
        '''sempre vai excluir o topo!'''
        if self.topo == None:
            print("Lista vazia!")
        else:
            self.topo = self.topo.prox
            self.tamanho -= 1

    def getTamanho(self):
        return self.tamanho

    def show(self):
        if self.topo == None:
            print("Lista vazia")
        else:
            temp = self.topo
            while(temp != None):
                temp.produto.mostrar()
                #taxa = 10/100
                #desconto = temp.produto.preco*taxa
                #temp.produto.preco -= desconto
                temp = temp.prox

listaProdutos = Lista()
for i in range(5):
    listaProdutos.add(Produto(int(input("digite codigo: ")), float(input("digite preco: ")), int(input("digite quantidade: "))))


print(listaProdutos.getTamanho())
listaProdutos.show()
print("\n")
listaProdutos.excluir()
listaProdutos.show()
print(listaProdutos.getTamanho())