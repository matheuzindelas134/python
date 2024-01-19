class Veiculo:
    def __init__(self, marca: str, modelo: str, ano:int , cor:str) :
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor 

class carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        super().__init__(marca, modelo, ano, cor)
        self.qtdPortas = qtdPortas 

class Bike(Veiculo)
    def __init__(self, marca: str, modelo: str, ano: int, cor: str):
        super().__init__(marca, modelo, ano, cor)
        self.relacao = relacao 

carro1 = Carro(marca ="ford", modelo = "ka", ano = 2020, cor= "azul", qtdPortas = 4)

bicicleta1 = Bike(marca = "canodale", modelo= " f1000", ano = 2020, cor= "azul", relacao = "shimano XT")

print(bicicleta1.ano)
