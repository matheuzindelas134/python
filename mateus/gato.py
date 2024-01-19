class Animal:
    def __init__(self, nome: str, raca: str, idade: float, castrado:bool):
        self.nome = nome
        self.raca = raca 
        self.idade = idade 
        self.castrado = castrado 
    
    def Miar(self):
        return f"O {self.nome}, esta miando, dê atenção a pra ele"
    
gato1 = Animal(nome = "mateus", raca = "siames", idade = 5 castrado =True)
gato2 = Animal(nome = "jade" , raca = "siames", idade = 8 castrado =False)

print(gato1.Miar())
print(gato2.Miar())
