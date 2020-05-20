from heapdict import heapdict

import numpy
from enum import Enum
import time


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


class AStar:
    def __init__(self, matrix):
        self.matrix = matrix

    # H Cuanto esta de lejos del nodo final
    def h(self, row, colum):
        if row == colum:
            return 0
        return self.matrix[row][colum]
        pass

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
        print(total_path)

    def resolve(self, start, goal):
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
                return self.reconstruct_path(came_from, current_name)

            for neighbor, column in enumerate(self.matrix[current_postition]):
                city = C(neighbor)
                tentative_g_score = g_score[current_name] + self.matrix[current_postition][neighbor]
                if tentative_g_score < g_score[city.name]:
                    g_score[city.name] = tentative_g_score
                    tentative_f_score = g_score[city.name] + self.h(neighbor, goal.value)
                    came_from[city.name] = current_name
                    open_set[city] = tentative_f_score


class Dijkstra:
    def __init__(self, matrix):
        self.matrix = matrix

    def reconstruct_path(self, came_from, current, start):
        total_path = [current.name]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current.name)
            if current == start:
                break
        print(total_path)

    def distanceToNextNode(self, current, neighbor):
        if current == neighbor:
            return 0
        return self.matrix[current][neighbor]

    def resolve(self, start, goal):
        q = heapdict()  # Dentro tiene la distancia
        prev = {}
        dist = {}
        for city in C:
            dist[city] = 999999999
            q[city] = 999999999
            prev[city] = -1
        q[start] = 0
        dist[start] = 0
        prev[start] = start

        while len(q) != 0:
            current = q.popitem()
            current_postition = current[0].value
            current_city = C(current_postition)

            for neighbor, column in enumerate(self.matrix[current_postition]):
                actualCity = C(neighbor)
                alt = dist[current_city] + self.distanceToNextNode(current_postition, neighbor)
                if alt < dist[actualCity]:
                    dist[actualCity] = alt
                    prev[actualCity] = current_city
                    q[current_city] = alt

        print(dist[goal])
        self.reconstruct_path(prev, goal, start)


if __name__ == '__main__':
    matrix = numpy.loadtxt(open("data.csv", "rb"), delimiter=",", skiprows=1, dtype=int)

    astar = AStar(matrix)
    disktra = Dijkstra(matrix)
    for city in C:
        for city2 in C:
            print("From :" + city.name + "\t" "to :" + city2.name)

            start = time.time()
            astar.resolve(city, city2)
            end = time.time()
            aStarTime = end - start

            start = time.time()
            disktra.resolve(city, city2)
            end = time.time()
            disktraTime = end - start

            if aStarTime < disktraTime:
                print("Star Wins again")
                timeEnd = ((disktraTime / aStarTime) * 100)
                print("Un " + str(timeEnd) + " mas rapido")
            else:
                print("Distra Wins again")
                print("Un " + str(timeEnd) + " mas rapido")
