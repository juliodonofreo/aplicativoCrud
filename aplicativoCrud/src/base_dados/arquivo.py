import csv

from entidades.consulta import Consulta
from entidades.enums.gravidade import Gravidade


def carregar_arquivo(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            reader = csv.reader(arquivo)
            lista = [Consulta(i[1], int(i[2]), i[3], i[4], Gravidade(int(i[5])), int(i[0])) for i in reader]
            return lista
    except IndexError:
        with open(caminho, 'w') as arquivo:
            return []


def salvar_dados(lista, caminho):
    Consulta.reset_id()
    with open(caminho, 'w', newline="\n") as arquivo:
        for consulta in lista:
            arquivo.write(f"{consulta.id},{consulta.nome_paciente},{consulta.idade_paciente},{consulta.nome_medico},{consulta.data_consulta},{consulta.gravidade.value}\n")
