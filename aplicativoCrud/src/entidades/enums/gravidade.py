from enum import Enum


class Gravidade(Enum):

    NAO_URGENTE = 1
    POUCO_URGENTE = 2
    URGENTE = 3
    MUITO_URGENTE = 4
    EMERGENCIA = 5

    def __str__(self):
        return f"{self.name}"
