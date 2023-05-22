import statistics
import time
from pathlib import Path

from aplicacao.validacoes import validacoes
from base_dados import arquivo

caminho = Path(__file__).parent.parent.parent / "base_dados" / "dados.txt"


def id_na_lista(lista, id):
    lista_ids = [i.id for i in lista]
    id_minimo = int(min(lista_ids))
    id_maximo = int(max(lista_ids))
    if id_minimo < id <= id_maximo:
        return True
    else:
        return False


def adicionar_consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade):
    global caminho
    lista = arquivo.carregar_arquivo(caminho)
    consulta = arquivo.Consulta(nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade)

    lista.append(consulta)
    arquivo.salvar_dados(lista, caminho)


def ler_tudo():
    lista = arquivo.carregar_arquivo(caminho)
    for i in lista:
        time.sleep(1)
        print(i)
        print()
    input("Digite enter para continuar: ")


def ler_por_id(id):
    lista = arquivo.carregar_arquivo(caminho)
    if id_na_lista(lista, id):
        return lista[id - 1]
    else:
        return None


def atualizar_consulta(id):
    lista = arquivo.carregar_arquivo(caminho)
    if id_na_lista(lista, id):
        consulta = lista[id - 1]
        consulta.nome_paciente = validacoes.validar_nome("Novo nome do paciente: ")
        consulta.idade_paciente = validacoes.validar_inteiro("Nova idade do paciente: ")
        consulta.nome_medico = validacoes.validar_nome("Novo nome do médico: ")
        consulta.data_consulta = validacoes.validar_data("%d/%m/%Y", "Nova data da consulta (dd/mm/yyyy): ")
        consulta.gravidade = validacoes.validar_gravidade("Novo nivel de Gravidade["
                                                          "verde/amarelo/vermelho/emergência]: ")
        lista[id - 1] = consulta
        arquivo.salvar_dados(lista, caminho)
        print("Atualização feita com sucesso! ")
    else:
        print("Id não encontrado. ")
    time.sleep(1)


def deletar_consulta(id):
    lista = arquivo.carregar_arquivo(caminho)
    if id_na_lista(lista, id):
        del(lista[id - 1])
        print("Deleção realizada com sucesso! ")
        arquivo.salvar_dados(lista, caminho)
    else:
        print("Id não encontrado. ")


def tendencia_central():
    lista = arquivo.carregar_arquivo(caminho)
    lista_idades = [i.idade_paciente for i in lista]
    print("Media de idades: ", round(statistics.mean(lista_idades), 2))
    print("Moda das idades: ", statistics.multimode(lista_idades))
    print("Mediana das idades: ", statistics.median(lista_idades))
    print("Variancia das idades: ", round(statistics.variance(lista_idades), 2))
    print("Desvio padrão das idades: ", round(statistics.stdev(lista_idades), 2))
    input("Digite enter para continuar: ")

