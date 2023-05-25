import time

import interface
from entidades.enums import gravidade
from aplicacao.operacoes import crud
from validacoes import validacoes


def limpar_tela():
    print("\n" * 100)


if __name__ == "__main__":

    while True:
        limpar_tela()
        valor = interface.menu_inicial()

        if 1 == valor:
            limpar_tela()

            nome_paciente = validacoes.validar_nome("digite o nome do paciente: ")
            idade_paciente = validacoes.validar_idade("digite a idade do paciente: ")
            nome_medico = validacoes.validar_nome("digite o nome do medico: ")
            data_consulta = validacoes.validar_data("%d/%m/%Y", "Digite a data da consulta (dd/mm/yyyy): ")
            gravidade = validacoes.validar_gravidade("digite o nivel de Gravidade["
                                                     "verde/amarelo/vermelho/emergência]: ")
            crud.adicionar_consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade)
        elif 2 == valor:
            limpar_tela()
            crud.ler_tudo()
        elif 3 == valor:
            limpar_tela()
            id = validacoes.validar_inteiro("Digite o id para a busca: ")
            consulta = crud.ler_por_id(id)
            if consulta is not None:
                print(consulta)
            else:
                print("Id não encontrado. ")
            input("\nDigite enter para continuar: ")
        elif 4 == valor:
            limpar_tela()
            id = validacoes.validar_inteiro("Digite o id para atualizar: ")
            crud.atualizar_consulta(id)
        elif 5 == valor:
            id = validacoes.validar_inteiro("Digite o id para deletar [0 cancela]: ")

            if id != 0:
                crud.deletar_consulta(id)
            else:
                print("Cancelado com sucesso! ")
            time.sleep(1)
        elif 6 == valor:
            crud.tendencia_central()
            time.sleep(1)
        else:
            break