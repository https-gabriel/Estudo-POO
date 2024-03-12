class Usuario:
    def __init__(self, firstName):
        self.firstName = firstName

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getFirstName(self):
        return "O seu primeiro nome é: " + self.firstName

userOne = Usuario("Joe")

print(userOne.getFirstName())