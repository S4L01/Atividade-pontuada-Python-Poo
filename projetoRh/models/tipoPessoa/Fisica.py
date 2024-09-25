from models.enums.Sexo import Sexo
from models.enums.EstadoCivil import EstadoCivil
from models.tipoPessoa.Pessoa import Pessoa
from models.Endereco import Endereco

from abc import ABC,abstractmethod


class Fisica(ABC,Pessoa):
    def __init__(self, id: int, nome: str,dataNascimento:str,sexo:Sexo,estadoCivil:EstadoCivil ,telefone: str, email: str ,endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.dataNascimento = dataNascimento
        self.estadoCivil = estadoCivil
        self.sexo = sexo

    def __str__(self) -> str:
        return super().__str__(f"\nData Nascimento:{self.dataNascimento}"
                               f"\nEstado Civil:{self.estadoCivil}"
                               f"\nSexo:{self.sexo}"
                               )