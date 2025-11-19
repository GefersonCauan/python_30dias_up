# Você foi designado pra criar um script interno que ajude o RH a controlar informações de funcionários sem depender de planilhas manuais.
# A ideia é ter um mini-sistema que possa:
# Cadastrar funcionários,
# Atualizar informações,
# # Consultar e listar todos
# Regras
# Cada funcionário tem um ID único (autoincremental).
# Permite alterar nome, cargo ou salário.
# Permite buscar pelo nome.
# Ao listar, mostrar em formato legível, ex: ID: 1 | Nome: João | Cargo: Analista | Salário: 3000

class Funcionario:
    _id_counter = 1

    def __init__(self, nome, cargo, salario):
        self.id = Funcionario._id_counter
        Funcionario._id_counter += 1
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def atualizar_info(self, nome=None, cargo=None, salario=None):
        if nome:
            self.nome = nome
        if cargo:
            self.cargo = cargo
        if salario:
            self.salario = salario
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Cargo: {self.cargo} | Salário: {self.salario}"
class RH:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self, nome, cargo, salario):
        novo_funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} cadastrado com ID {novo_funcionario.id}.")

    def atualizar_funcionario(self, id, nome=None, cargo=None, salario=None):
        for func in self.funcionarios:
            if func.id == id:
                func.atualizar_info(nome, cargo, salario)
                print(f"Funcionário ID {id} atualizado.")
                return
        print(f"Funcionário com ID {id} não encontrado.")

    def buscar_por_nome(self, nome):
        resultados = [func for func in self.funcionarios if func.nome.lower() == nome.lower()]
        if resultados:
            for func in resultados:
                print(func)
        else:
            print(f"Nenhum funcionário encontrado com o nome {nome}.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for func in self.funcionarios:
            print(func)

# Exemplo de uso
if __name__ == "__main__":
    rh = RH()
    rh.cadastrar_funcionario("João", "Analista", 3000)
    rh.cadastrar_funcionario("Maria", "Desenvolvedora", 4000)
    rh.listar_funcionarios()
    rh.atualizar_funcionario(1, salario=3500)
    rh.buscar_por_nome("Maria")
    rh.listar_funcionarios()