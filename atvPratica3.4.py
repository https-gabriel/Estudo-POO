"""Crie uma classe chamada Robo(). Ela deverá ter duas propriedades privadas: nome e
ano_construcao. Também deverá ter um método de nome “diga_alo()”, para mostrar na
tela o nome do robô e seu ano de construção. Crie os métodos “setters” e “getters”
necessários. Instancie a classe e use os métodos criados para visualizar / atualizar os dados."""

class Robo():
    def __init__(self, nome, ano_construcao):
        self.nome = nome
        self.ano_construcao = ano_construcao
    
    def setRobo(self, nome, ano_construcao):
        self.__nome = nome
        self.__ano_contrucao = ano_construcao
    
    def getDiga(self):
        return "hi, my name is "+ self.nome + "my frabication he was " + self.ano_construcao

robo = Robo("Theo", "01/01/0001")

print(robo.getDiga())