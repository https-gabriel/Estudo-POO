"""
1. Acrescente à classe Usuario um método construtor para definir um valor para a propriedade
primeiroNome assim que o objeto for criado.
2. Acrescente ao construtor a capacidade de definir o valor da propriedade ultimoNome, bem como a
propriedade primeiroNome.
3. Adicione à classe Usuario um método chamado getNomeCompleto() que retorna o nome
completo do usuário.
4. Crie um novo objeto, usuario1, e passe para o construtor os valores do primeiro e último nome. O
primeiro nome é "Johnny" e o sobrenome é "Bravo" (você pode escolher sua combinação preferida
de primeiro e último nome).
5. Obtenha o nome completo e imprima-o na tela.
"""

class Users():
    firstName = ""
    lastName = ""

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return self.firstName + " " + self.lastName


user1 = Users( "gabriel", "farias")

print(user1.getFullName())