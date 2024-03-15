"""Implemente uma classe chamada Pessoa que tenha dois atributos privados chamados
“primeiroNome” e “ultimoNome”, respectivamente. Em seguida, implemente métodos
chamados “getPrimeiroNome()” e “getUltimoNome()”, para ler os atributos, e os
métodos “setPrimeiroNome()” e “setUltimoNome()” para atribuir valores a eles. Depois
crie uma instância da classe Pessoa definindo os seguintes valores:
primeiroNome = 'João'
ultimoNome = 'Carvalho'"""

class Pessoa():
    def __init__(self, primeiroNome, segundoNome):
        self.primeiroNome = primeiroNome;
        self.segundoNome = segundoNome;

    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    def getPrimeiroNome(self):
        return self.__primeiroNome
    def setsegundoNome(self, segundoNome):
        self.__segundoNome = segundoNome
    def getsegundoNome(self):
        return self.__segundoNome



pessoa = Pessoa("", "");


pessoa.setPrimeiroNome("João");
pessoa.setsegundoNome("Carvalho");

print(pessoa.getPrimeiroNome())
print(pessoa.getsegundoNome())