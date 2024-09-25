from abc import ABC
from projetoRh.models.tipoPessoa.Fisica import Fisica
from projetoRh.models.Endereco import Endereco
from projetoRh.models.enums.EstadoCivil import EstadoCivil
from projetoRh.models.enums.Sexo import Sexo
from projetoRh.models.enums.Setor import Setor

class Funcionario(ABC,Fisica):
    def __init__(self, id: int, nome: str, dataNascimento: str, sexo: Sexo, estadoCivil: EstadoCivil, telefone: str, cpf:str,rg:str,matricula:str,setor:Setor,salario:float,email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, dataNascimento, sexo, estadoCivil, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return super().__str__(f"\nCpf:{self.cpf}"
                               f"\nRg:{self.rg}"
                               f"\nMatricula:{self.matricula}"
                               f"\nSetor:{self.setor}"
                               f"\nSalario:{self.salario}"
                               )