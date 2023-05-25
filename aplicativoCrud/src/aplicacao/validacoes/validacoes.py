from datetime import datetime

from entidades.enums import gravidade


def validar_inteiro(msg=""):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("valor inválido, por favor digite novamente. ", end="")
        else:
            return valor


def validar_idade(msg=""):
    while True:
        idade = validar_inteiro(msg)

        if idade < 0:
            print("A idade não pode ser um valor negativo. ", end="")
        elif idade > 200:
            print("Digite uma data válida. ", end="")
        else:
            return idade


def validar_data(fmt, msg=""):
    while True:
        try:
            valor = datetime.strptime(input("Digite a data da consulta (dd/mm/yyyy): "), fmt).date()
        except ValueError:
            print("Formato de data inválido, por favor digite novamente. ", end="")
        else:
            return valor


def validar_nome(msg=""):
    while True:
        nome: str = str(input(msg)).capitalize()
        if nome == '':
            print('o nome não pode ficar vazio.', end='')
        elif not nome.replace(' ', '').isalpha():
            print('o nome deve conter apenas letras. ', end='')
        elif len(nome) < 2:
            print('o nome precisa ter ao menos duas letras. ', end='')
        else:
            return nome


def validar_gravidade(msg=""):
    while True:
        try:
            tipo_gravidade = gravidade.Gravidade[input(msg).upper().replace("Ê", "E")]
        except KeyError:
            print("Digite uma gravidade válida. ", end="")
        else:
            return tipo_gravidade
