from projetoRh.models.Endereco import Endereco
from projetoRh.models.tipoPessoa.Juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, cnpj: str, contratoFim:str,contratoInicio:str,inscricaoEstadual: str, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, cnpj, inscricaoEstadual, email, endereco)
        self.contratoFim = contratoFim
        self.contratoInicio = contratoInicio

    def __str__(self) -> str:
        return super().__str__(f"\nContrato Inicio:{self.contratoInicio}"
                               f"\nContrato Fim:{self.contratoFim}"
                               )        
