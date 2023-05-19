from datetime import datetime

from entidades.enums.gravidade import Gravidade


class Consulta:
    __index: int = 1

    __id: int
    __nome_paciente: str
    __idade_paciente: int
    __nome_medico: str
    __data_consulta: datetime
    __gravidade: Gravidade

    def __init__(self,  nome_paciente, idade_paciente, nome_medico, data_consulta, gravidade, id = None):
        if id is None:
            self.__id = Consulta.__index
            Consulta.__index += 1
        else:
            self.__id = id

        self.__nome_paciente = nome_paciente
        self.__idade_paciente = idade_paciente
        self.__nome_medico = nome_medico
        self.__data_consulta = data_consulta
        self.__gravidade = gravidade

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome_paciente(self):
        return self.__nome_paciente

    @nome_paciente.setter
    def nome_paciente(self, nome_paciente):
        self.__nome_paciente = nome_paciente

    @property
    def idade_paciente(self):
        return self.__idade_paciente

    @idade_paciente.setter
    def idade_paciente(self, idade_paciente):
        self.__idade_paciente = idade_paciente

    @property
    def nome_medico(self):
        return self.__nome_medico

    @nome_medico.setter
    def nome_medico(self, nome_medico):
        self.__nome_medico = nome_medico

    @property
    def data_consulta(self):
        return self.__data_consulta

    @data_consulta.setter
    def data_consulta(self, data_consulta):
        self.__data_consulta = data_consulta

    @property
    def gravidade(self):
        return self.__gravidade

    @gravidade.setter
    def gravidade(self, gravidade):
        self.__gravidade = gravidade

    @classmethod
    def reset_id(cls):
        cls.__id = 1

    def __repr__(self) -> str:
        return f"{self.__id}, {self.nome_paciente}, {self.idade_paciente}, {self.nome_medico}, {self.data_consulta}, {self.gravidade}"

    def __str__(self):
        return f"id: {self.id}\n" \
               f"Nome do paciente: {self.nome_paciente}\n" \
               f"Idade do paciente: {self.idade_paciente}\n" \
               f"Nome do médico: {self.nome_medico}\n" \
               f"Data da consulta: {self.data_consulta}\n" \
               f"Gravidade: {self.gravidade.name}"






