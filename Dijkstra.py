import time

from heapdict import heapdict

from Cities import C


class Dijkstra:
    def __init__(self, matrix):
        self.matrix = matrix

    def reconstruct_path(self, came_from, current, start):
        total_path = [current.name]
        while current in came_from.keys():
            current = came_from[current]
            if current.name not in total_path:
                total_path.insert(0, current.name)
            if current == start:
                break
        return total_path

    def distanceToNextNode(self, current, neighbor):
        if current == neighbor:
            return 0
        return self.matrix[current][neighbor]

    def resolve(self, start, goal):
        startTime = time.time()
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
        endTime = time.time()
        return dist[goal], self.reconstruct_path(prev, goal, start), endTime - startTime
