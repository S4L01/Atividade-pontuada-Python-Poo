from abc import ABC,abstractmethod
from projetoRh.models.tipoPessoa.Pessoa import Pessoa
from projetoRh.models.Endereco import Endereco

class Juridica(ABC,Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, cnpj:str,contratoFim:str,email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj 
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return super().__str__(f"\nCnpj:{self.cnpj}"
                               f"\nFim do Contrato:{self.contratoFim}"
                               )         
