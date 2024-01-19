class Animal:
    def __init__(self, nome:str,raca:str,idade:int,cor:str):
        self.nome = nome 
        self.raca = raca
        self.idade = idade
        self.cor = cor 

    def emitirSom(self):
        return "Som indefinido"
    
class Gato(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    def emitirSom(self):
        return "miauu"
    
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    def emitirSom(self):
        return "rouf rouf"
    
gatinho = Gato(nome= "xana", raca= "siames", idade= 2, cor="marrom")
cachorro = Cachorro(nome= "calzone", raca= "pitbul", idade= 2, cor="marrom")
porco = Animal(nome="Bacon", raca="PERDIGAO", idade = 1, cor= "rosa")


print(gatinho.emitirSom())
print(cachorro.emitirSom())
print(porco.emitirSom())
