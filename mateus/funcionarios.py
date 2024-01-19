from datetime import datetime

class Funcionarios:
    def __init__(self, nome = str, cpf= str, idade = int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        
    def bater_ponto(self):
        horario = datetime.now()
        horario_formatado = horario.strftime("%H:%M")
        return f"O {self.nome} bateu o ponto {horario} horas"
    
class Gerente(Funcionarios):
    def __init__(self, nome=str, cpf=str, idade=int):
        super().__init__(nome, cpf, idade)
    def demitir(self):
        return f"o {self.nome} demitiu um funcionario"
    def contratar(self):
        return f"o {self.nome} contratou alguem"
    

class Caixa(Funcionarios):
    def __init__(self, nome=str, cpf=str, idade=int,num_do_caixa= int):
        super().__init__(nome, cpf, idade)
        self.num_do_caixa = num_do_caixa
        
    def fechar(self):
        return f"o caixa {self.nome} fechou o caixa {self.num_do_caixa}"
        

gerente1 = Gerente( nome = "matheus", cpf =62455452520, idade = 20)
caixa1 = Caixa(nome= "pedro", cpf="12345678900", idade= 21, num_do_caixa= 5 )

print(gerente1.demitir())
print(gerente1.bater_ponto())

print(caixa1.fechar())
print(caixa1.bater_ponto())

    
    