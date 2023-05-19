from datetime import datetime


def validar_inteiro(msg=""):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print("valor inválido. por favor digite novamente. ", end="")
        else:
            return valor


def validar_data(fmt, msg=""):
    while True:
        try:
            valor = datetime.strptime(input("Digite a data da consulta (dd/mm/yyyy): "), fmt).date()
        except ValueError:
            print("Formato de data inválido, por favor digite novamente. ", end="")
        else:
            return valor

