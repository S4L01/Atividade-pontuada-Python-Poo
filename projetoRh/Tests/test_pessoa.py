import pytest
from ..models.tipoPessoa.Pessoa import Pessoa
from ..models.Endereco import Endereco
from ..models.enums.UnidadeFederativa import UnidadeFederativa
@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(12,"salo","7198888",18,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))
    return pessoa
def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "salo"

def test_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 18

def test_idade_negativa_erro():
    with pytest.raises(ValueError,match="A idade não pode ser negativa."):
        Pessoa(12,"salo","7198888",-18,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))   

def test_idade_acima130_erro():
    with pytest.raises(ValueError,match="A idade não pode ser acima de 130."):
        Pessoa(12,"salo","7198888",131,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))   

def test_idade_tipoInvalido_erro():
    with pytest.raises(ValueError,match="A idade deve ser um número inteiro."):
        Pessoa(12,"salo","7198888",131,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))   

def test_nome_tipoInvaldo_erro():
    with pytest.raises(ValueError,match="O nome deve ser um texto."):
        Pessoa(12,12,"7198888",131,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))   

def test_nome_vazio_erro():
    with pytest.raises(ValueError,match="O nome não deve estar vazio."):
        Pessoa(12,"","7198888",131,"@algumacoisa",
                    Endereco("Ao lado de algo","121","subida","40500","salvador",UnidadeFederativa.BAHIA))   

