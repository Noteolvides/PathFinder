import time
from heapdict import heapdict

from Cities import C


class BFS:
    def __init__(self, matrix):
        self.matrix = matrix

    def distanceToNextNode(self, current, neighbor):
        if current == neighbor:
            return 0
        return self.matrix[current][neighbor]

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
        visited = {}
        for city in C:
            visited[city] = 0
        visited[start] = 1
        came_from = {}

        while len(open_set) != 0:
            current = open_set.popitem()  # Obtenemos una city y su f_score
            current_postition = current[0].value
            current_name = current[0].name
            if current_postition == goal.value:
                endTime = time.time()
                return current[1], self.reconstruct_path(came_from, current_name), endTime - startTime

            for neighbor, column in enumerate(self.matrix[current_postition]):
                city = C(neighbor)
                if visited[city] != 1 and column < 99999:
                    visited[city] = 1
                    came_from[city.name] = current_name
                    open_set[city] = self.distanceToNextNode(neighbor, goal.value)
