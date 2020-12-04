from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

        def get_cpf(self):
            return self.cpf

        def set_cpf(self, cpf):
            self.cpf = cpf