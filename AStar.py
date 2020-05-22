import time

from heapdict import heapdict

from Cities import C


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
        return total_path

    def resolve(self, start, goal):
        startTime = time.time()
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
                endTime = time.time()
                return current[1], self.reconstruct_path(came_from, current_name), endTime - startTime

            for neighbor, column in enumerate(self.matrix[current_postition]):
                city = C(neighbor)
                tentative_g_score = g_score[current_name] + self.matrix[current_postition][neighbor]
                if tentative_g_score < g_score[city.name]:
                    g_score[city.name] = tentative_g_score
                    tentative_f_score = g_score[city.name] + self.h(neighbor, goal.value)
                    came_from[city.name] = current_name
                    open_set[city] = tentative_f_score
