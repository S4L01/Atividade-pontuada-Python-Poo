from abc import ABC
from ..Endereco import Endereco
class Pessoa(ABC):
        def __init__(self,id:int,nome:str,telefone:str,idade:int,email:str,endereco:Endereco) -> None:
                self.id = id
                self.nome = self._vericacao_nome(nome)
                self.telefone= telefone
                self.email = email
                self.endereco = endereco
                self.idade = self._verificacao_idade(idade)

        def _vericacao_nome(self,erroNome):
                self.verificar_nome_invalido(erroNome)
                self.verificar_nome_vazio(erroNome)

                self.nome = erroNome
                return self.nome                

        def _verificacao_idade(self,erroIdade):
                self.verificar_idade_invalido(erroIdade)
                self.verificar_idade_maisDe130(erroIdade)
                self.verificar_idade_invalido_negativo(erroIdade)

                self.idade = erroIdade
                return erroIdade
        
        #metodos para verificaçao
        def verificar_idade_invalido(self,erroIdade):
                if not isinstance(erroIdade,int):  
                        raise TypeError("A idade deve ser um valor inteiro.")
        
        def verificar_idade_invalido_negativo(self,erroIdade):
                if erroIdade <= 0:
                        raise ValueError("A idade não pode ser negativa")
        
        def verificar_idade_maisDe130(self,erroIdade):
                if erroIdade > 130:
                        raise ValueError("A idade não pode ser maior que 130")

        def verificar_nome_invalido(self,erroNome):
                if not isinstance(erroNome,str):
                        raise TypeError("O nome deve ser um texto")

        def verificar_nome_vazio(self,erroNome):
                if not erroNome.strip():
                        raise TypeError("O nome não deve estar vazio")
                


        def __str__(self) -> str:
                return (f"\nId:{self.id}"
                        f"\nNome:{self.nome}"
                        f"\nTelefone:{self.telefone}"
                        f"\nEmail:{self.email}"
                        f"\nEndereco:{self.endereco}"
                        )                