from heapq import heapify
from heapq import heappop
from heapq import heappush
from heapdict import heapdict

import numpy
from enum import Enum

matrix = []


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


# H Cuanto esta de lejos del nodo final
def h(row, colum):
    if row == colum:
        return 0
    return matrix[row][colum]
    pass


def exists(heap, item, score):
    for i, x in enumerate(heap):
        if x[1] == item:
            heap[i] = (score, item)
            heapify(heap)
            return True
    return False


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    print(total_path)


def a_start(start, goal):
    open_set = heapdict()
    open_set[start] = 0
    came_from = {}
    # g() cuando de lejos del nodo inicial
    g_score = {}
    for city in C:  # Inicializamos en infinito para hacer poda
        g_score[city.name] = 999999999
    g_score[start.name] = 0  # El nodo inicial no esta lejos de si mismo

    while len(open_set) != 0:
        current = open_set.popitem()  # Obtenemos una city y su f_score
        current_postition = current[0].value
        current_name = current[0].name
        if current_postition == goal.value:
            print(current[1])
            return reconstruct_path(came_from, current_name)

        for neighbor, column in enumerate(matrix[current_postition]):
            city = C(neighbor)
            tentative_g_score = g_score[current_name] + matrix[current_postition][neighbor]
            if tentative_g_score < g_score[city.name]:
                g_score[city.name] = tentative_g_score
                tentative_f_score = g_score[city.name] + h(neighbor, goal.value)
                came_from[city.name] = current_name
                open_set[city] = tentative_f_score


if __name__ == '__main__':
    matrix = numpy.loadtxt(open("data.csv", "rb"), delimiter=",", skiprows=1, dtype=int)
    for city in C:
        for city2 in C:
            a_start(city, city2)
