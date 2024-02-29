"""Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe estando dentro dela? A resposta é palavra-chave self 

Exercício de Codificação
Na atividade prática anterior, escrevemos o método hello() dentro da classe Usuario. No exercício a
seguir, adicionaremos a este método a capacidade de acessar as propriedades da classe com a palavra-chave
self.
A classe Usuario poderia ser codificada assim:
class Usuario():
# as propriedades
primeiroNome = “”
ultimoNome = “”
#metodo que diz Olá ao usuario
def hello(self)
return "Olá"

2. Acrescente ao método hello() a capacidade de acessar a propriedade primeiroNome, para que
o método possa retornar a string "Olá, primeiroNome".
3. Crie um novo objeto com o primeiro nome de "Jonnie" e sobrenome de "Bravo".
4. Use o comando print no método hello() para o objeto usuario1 e observe o resultado.
"""

class User:
    firstName = "Jonny"
    lastName = "Bravo"
    
    def hello(self):
        return "Hello" + " " + self.firstName + " " + self.lastName


user = User()

print(user.hello())