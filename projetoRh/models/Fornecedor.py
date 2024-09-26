from projetoRh.models.Endereco import Endereco
from projetoRh.models.tipoPessoa.Juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, cnpj: str, produto:str,inscricaoEstadual: str, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, cnpj, inscricaoEstadual, email, endereco)
        self.produto = produto
    def __str__(self) -> str:
        return super().__str__(f"\nProduto:{self.produto}")        