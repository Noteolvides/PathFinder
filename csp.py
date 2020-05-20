from heapq import heapify, heappop, heappush
from data import matrix

def csp_start(start, goal):
    if start.name == goal.name:
        print(0)
        return 0
    open_set = [start]
    heapify(open_set)

    found = False
    while not found:
        current = heappop(open_set)
        # pillar las siguientes ciudades
        for city in matrix[current]:
            heappush(open_set, city)
        # comprobaciones de restricciones