"""
Implemente uma classe chamada Laptop que possua um atributo privado chamado “preco”
que armazena o preço do laptop (sem qualquer validação). Em seguida, implemente um método
para ler esse atributo chamado “get_preco()” e um método para modificar esse atributo
chamado “set_preco()” sem validação também. Em seguida, crie uma instância da classe
Laptop siga estas etapas:
• usando o método “get_preco()” imprima o valor do atributo “preco” na tela
• usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”
"""

class Laptop():
    def __init__(self, preco):
        self.preco = preco
    def setpreco(self, preco):
        self.__preco = preco
    def getpreco(self):
        return self.__preco
    
laptop = Laptop("")
laptop.setpreco("123")
print(laptop.getpreco())
