import interface
from datetime import datetime
from entidades.enums import gravidade
from aplicacao.operacoes import crud
from validacoes import validacoes


def limpar_tela():
    print("\n" * 100)


if __name__ == "__main__":

    while True:
        limpar_tela()
        valor = interface.menu()

        if 1 == valor:
            limpar_tela()

            nome_paciente = input("digite o nome do paciente: ")
            idade_paciente = validacoes.validar_inteiro("digite a idade do paciente: ")
            nome_medico = input("digite o nome do medico: ")
            data_consulta = validacoes.validar_data("%d/%m/%Y", "Digite a data da consulta (dd/mm/yyyy): ")
            gravidade = gravidade.Gravidade[input("digite o nivel de Gravidade: ").upper()]
            crud.adicionar_consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade)
        if 2 == valor:
            limpar_tela()
            crud.ler_tudo()
        if 3 == valor:
            limpar_tela()
            id = validacoes.validar_inteiro("Digite o id para a busca: ")
            print(crud.ler_por_id(id))
