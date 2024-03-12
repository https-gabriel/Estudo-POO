"""Crie uma classe chamada Empregado(), com três propriedades: nome, salario (deve ser
privada) e projeto. Ela também possui um método chamado “trabalho()”, que deverá
imprimir o nome do funcionário e o projeto em que ele está trabalhando e um outro método
chamado “mostrar()” para exibir os detalhes desse empregado (i.e. nome e salário). Atente
para o modificador de acesso da propriedade “salario”. Use o método adequado para ter
acesso a ela. Crie um objeto desta classe (i.e. instância) e use os métodos para visualizar os
dados."""

class Empregado():
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.salario = salario
        self.projeto = projeto
    
    def setEmpregado(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    def getTrabalho(self):
        return "O nome do empregado é " + self.nome + "e ele está no prjeto " + self.projeto
    
empregado = Empregado("teste", "", "Desenvolvimento Web 3.0")

print(empregado.getTrabalho())