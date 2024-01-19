class Veiculo:
    def __init__(self, marca: str, modelo: str, ano:int , cor:str) :
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor 
    def Ligar(self):
        return f"o veiculo {self.modelo} ligou"
        
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:int):
        super().__init__(marca, modelo, ano, cor)
        self.qted_portas = qtde_portas

    def cavalo_de_pau(self):
        return f"O carro {self.modelo} quem tem {self.qted_portas} de portas fez um cavalo de pau"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: int):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    
    def empinar(self):
        return f"A moto {self.modelo} de {self.cilindradas} cilindradas, chamou no grau"


carro1 = Carro(marca="fiat", modelo="uno", ano= 2004, cor="Azul escuro", qtde_portas = 2)
moto1 = Moto(marca="honda", modelo= "titan", ano = 2022, cor = "vermelho", cilindradas=160)


print(carro1.qted_portas)
print(moto1.cilindradas)


print(carro1.Ligar())
print(moto1.empinar())


