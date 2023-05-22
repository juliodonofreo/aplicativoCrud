from enum import Enum


class Gravidade(Enum):

    VERDE = 1
    AMARELO = 2
    VERMELHO = 3
    EMERGENCIA = 4

    def __str__(self):
        return f"{self.name}"
