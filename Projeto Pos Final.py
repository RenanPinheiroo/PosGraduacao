class Cliente:
    def __init__ (self, nome, Serviço, Data):
        self.nome = nome
        self.Serviço = Serviço
        self.Data = Data

Serviço = ["Extensão", "Manutenção", "Corte"]

class BaseClientes:
    def __init__ (self):
        self.clientes = []
  
    def adicionar_atendimento(self, nome):
        self.clientes.append(nome)

baseclientes = BaseClientes()
baseclientes.adicionar_atendimento(["Mariana"])


print(len(baseclientes.clientes))

    
cliente_1 = Cliente("Joana", "Manutenção", "30/03/2023")

print(cliente_1.nome)