from pathlib import Path

from base_dados.arquivo import *

caminho = Path(__file__).parent.parent.parent / "base_dados" / "dados.txt"


def adicionar_consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade):
    global caminho
    lista = carregar_arquivo(caminho)
    consulta = Consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade)

    lista.append(consulta)
    salvar_dados(lista, caminho)


def ler_tudo():
    lista = carregar_arquivo(caminho)

    for i in lista:
        print(i)


def ler_por_id(id):
    lista = carregar_arquivo(caminho)
    return lista[id - 1]
