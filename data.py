from heapq import heapify
from heapq import heappop
from heapq import heappush

import numpy
from enum import Enum

from csp import csp_start

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
    if start.name == goal.name:
        print(0)
        return 0
    open_set = [(0, start)]
    heapify(open_set)

    came_from = {}

    g_score = {}
    for city in C:
        g_score[city.name] = 999999999
    g_score[start.name] = 0
    f_score = {}
    for city in C:
        f_score[city.name] = 999999999
    f_score[start.name] = matrix[start.value][goal.value]

    while len(open_set) != 0:
        current = heappop(open_set)
        current_postition = current[1].value
        current_name = current[1].name

        if current_postition == goal.value:
            print(f_score[goal.name])
            return reconstruct_path(came_from, current_name)

        for neighbor, column in enumerate(matrix[current_postition]):
            city = C(neighbor)
            tentative_g_score = g_score[current_name] + matrix[current_postition][neighbor]
            if tentative_g_score < g_score[city.name]:
                g_score[city.name] = tentative_g_score
                tentative_f_score = g_score[city.name] + h(neighbor, goal.value)
                f_score[city.name] = tentative_f_score
                came_from[city.name] = current_name
                if not exists(open_set, city, tentative_f_score):
                    heappush(open_set, (f_score[city.name], city))


if __name__ == '__main__':
    matrix = numpy.loadtxt(open("data.csv", "rb"), delimiter=",", skiprows=1, dtype=int)
    a_start(C.BARCELONA, C.VALLADOLID)
    csp_start(C.BARCELONA, C.VALLADOLID)
