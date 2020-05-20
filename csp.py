import time
from heapq import heapify, heappop, heappush
from operator import attrgetter

from heapdict import heapdict

from Cities import C, City


class CSP:
    def __init__(self, matrix):
        self.matrix = matrix

    def reconstruct_path(self, came_from, current, start):
        #Añade el ultimo
        total_path = [current]
        # mientras no ha llegado a la ciudad inicial
        # va recorriendo el camino de atras a adelante
        while start.name != current:
            # Pilla el anterior y lo añade
            current = came_from[current]
            total_path.insert(0, current)

        return total_path

    def sortFunc(e):
        return e.valor

    def resolve(self, start, goal):
        startTime = time.time()
        stack = []
        current = City(start.name, start.value, 0)
        stack.append(current)
        # Hay que iniciarlo a la longitud que toca para que no pete al acceder
        visited = [False] * len(C)
        came_from = {}

        found = False
        while not found:
            # El nombre antiguo se guarda para tener bien las relaciones de came_from
            old_name = current.name
            # Devolvemos la ciudad con la mejor restriccion
            current = stack.pop()
            # Guardar valores varios de la ciudad actual
            current_postition = current.value
            current_name = current.name
            # Marcamos la ciudad actual como visitada
            visited[current_postition] = True
            # pillar las siguientes ciudades
            came_from[current_name] = old_name

            ordenar = []
            for neighbour, column in enumerate(self.matrix[current_postition]):
                # Si un vecino no es valido, no hace falta hacer los calculos de dentro
                if self.matrix[current_postition][neighbour] != 999999999 and not visited[neighbour]:
                    city = C(neighbour)
                    if city == goal:
                        # jajas
                        print("jajas")
                        came_from[city.name] = current_name

                        # TODO que el reconstruct calcule la longitud
                        return 100, self.reconstruct_path(came_from, goal.name, start), time.time() - startTime
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
            # TODO esta guardando el array. no los elementos
            # El extend seria un addAll de un array a otro
            stack.extend(ordenar)

    def calculo_restriccion(self, current_postition, neighbour, visited):
        salidas = self.exits(neighbour, visited)
        if salidas == 0:
            return -1
        return self.matrix[current_postition][neighbour] / salidas

    def exits(self, neighbour, visited):
        salidas = 0
        columna = 0
        while columna < len(self.matrix[neighbour]):
            if self.matrix[neighbour][columna] != 999999999 and not visited[columna]:
                salidas += 1
            columna += 1
        return salidas
