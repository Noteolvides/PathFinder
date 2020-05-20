from enum import Enum


class C(Enum):
    BARCELONA = 0
    MADRID = 1
    VALENCIA = 2
    SEVILLA = 3
    ZARAGOZA = 4
    MALAGA = 5
    MURCIA = 6
    BILBAO = 7
    VIGO = 8
    CORDOBA = 9
    VALLADOLID = 10
    HOSPITALET = 11


class City:
    def __init__(self, name, value, heuristica):
        self.name = name
        self.value = value
        self.heuristica = heuristica
