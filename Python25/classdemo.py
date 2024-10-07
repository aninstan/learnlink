
class Person:
    def __init__(self, navn, alder, kjønn):
        self.navn = navn
        self.alder = alder
        self.kjønn = kjønn

person1 = Person("Petter", 34, 'M')

print(person1.kjønn)