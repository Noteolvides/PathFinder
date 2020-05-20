import time
from heapq import heapify, heappop, heappush
from operator import attrgetter

from heapdict import heapdict

from Cities import C, City


class CSP:
    def __init__(self, matrix):
        self.matrix = matrix

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.insert(0, current)
        return total_path

    def sortFunc(e):
        return e.valor

    def resolve(self, start, goal):
        startTime = time.time()
        stack = []
        stack.append(City(start.name, start.value, 0))

        visited = {}
        came_from = {}


        found = False
        while not found:
            # Devolvemos la ciudad con la mejor restriccion
            current = stack.pop()
            # Guardar valores varios de la ciudad actual
            current_postition = current.value
            current_name = current.name
            # Marcamos la ciudad actual como visitada
            visited[current_postition] = True
            # pillar las siguientes ciudades
            came_from[current_name] = current_name

            ordenar = []
            for neighbour, column in enumerate(self.matrix[current_postition]):
                city = C(neighbour)
                if city == goal:
                    # came_from[city.name] = current_name
                    # TODO que el reconstruct calcule la longitud
                    return 100, self.reconstruct_path(came_from, current_name), time.time() - startTime
                # TODO, pensar como hacer la heuristica para ciudades que ya estan en la pila
                heuristica = self.calculo_restriccion(current_postition, neighbour, visited)

                if heuristica == -1:
                    visited[neighbour] = False
                    continue

                # TODO mirar si se puede hacer un add ordenado
                ordenar.append(City(city.name, city.value, heuristica))

            # TODO usar un quicksort miar para optimizar
            ordenar.sort(reverse=True, key=attrgetter('heuristica'))
            # TODO mirar si se puede guardar sin el value
            stack.append(ordenar)

    def calculo_restriccion(self, current_postition, neighbour, visited):
        salidas = self.exits(neighbour, visited)
        if salidas == 0:
            return -1
        return self.matrix[current_postition][neighbour] / salidas

    def exits(self, neighbour, visited):
        salidas = 0
        columna = 0
        while columna < len(self.matrix[neighbour]):
            if self.matrix[neighbour][columna] != 999999999: #and not visited[columna]:
                salidas += 1
            columna += 1
        return salidas
