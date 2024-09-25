from projetoRh.models.Endereco import Endereco
from projetoRh.models.enums.EstadoCivil import EstadoCivil
from projetoRh.models.enums.Sexo import Sexo
from projetoRh.models.tipoPessoa.Fisica import Fisica


class Cliente(Fisica):
    def __init__(self, id: int, nome: str, protocoloAtendimento:int,dataNascimento: str, sexo: Sexo, estadoCivil: EstadoCivil, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, dataNascimento, sexo, estadoCivil, telefone, email, endereco)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return super().__str__(f"\nProtocolo Atendimento:{self.protocoloAtendimento}")    