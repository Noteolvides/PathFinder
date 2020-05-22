import numpy
import time

from AStar import AStar
from Cities import C
from Dijkstra import Dijkstra
from BFS import BFS
from csp import CSP

if __name__ == '__main__':
    matrix = numpy.loadtxt(open("data.csv", "rb"), delimiter=",", skiprows=1, dtype=int)

    rightTimesStar = 0
    rightTimesBFS = 0
    totalCases = 0
    totalTimeStar = 0
    totalTimeBFS = 0
    totalTimeDist = 0
    totalTimeCSP = 0
    astar = AStar(matrix)
    disktra = Dijkstra(matrix)
    bfs = BFS(matrix)

    csp = CSP(matrix)

    # (costAstar, path, timeCSP) = csp.resolve(C.HOSPITALET, C.MURCIA)
    # print(str(path) + " - " + str(timeCSP))

    for city in C:
        for city2 in C:

            print("From :" + city.name + "\t" "to :" + city2.name)

            (costAstar, pathAStar, timeAStar) = astar.resolve(city, city2)
            print("Astart GOT: " + "Cost of:" + str(costAstar) + " Path of: " + str(pathAStar) + " Time of: " + str(
                timeAStar))

            (costDisk, pathDisk, timeDisk) = disktra.resolve(city, city2)
            print(
                "Disk GOT: " + "Cost of:" + str(costDisk) + " Path of: " + str(pathDisk) + " Time of: " + str(timeDisk))
            (costBfs, pathBfs, timeBfs) = bfs.resolve(city, city2)
            print(
                "Bfs GOT: " + "Cost of:" + str(costBfs) + " Path of: " + str(pathBfs) + " Time of: " + str(timeBfs))

            totalTimeBFS += timeBfs
            (costCSP, pathCSP, timeCSP) = csp.resolve(city, city2)
            print("CSP GOT: " + "Cost of:" + str(costCSP) + " Path of: " + str(pathCSP) + " Time of: " + str(
                timeCSP))

            totalTimeDist += timeDisk
            totalTimeStar += timeAStar
            totalTimeCSP += timeCSP
            if pathAStar == pathDisk:
                rightTimesStar += 1
            if pathBfs == pathDisk:
                rightTimesBFS += 1
            totalCases += 1

    print("Total Cases " + str(totalCases))
    print("Right Cases Star " + str(rightTimesStar))
    print("Right Percentaje " + str((rightTimesStar / totalCases) * 100) + "%")

    print("Right Cases BFS " + str(rightTimesBFS))
    print("Right Percentaje " + str((rightTimesBFS / totalCases) * 100) + "%")

    mediaTiempoBfs = totalTimeBFS / totalCases
    mediaTiempoStar = totalTimeStar / totalCases
    mediaTiempoDist = totalTimeDist / totalCases
    mediaTiempoCSP = totalTimeCSP / totalCases
    print("Media tiempo Star " + str(mediaTiempoStar))
    print("Media tiempo Disk " + str(mediaTiempoDist))
    print("Media tiempo CSP " + str(mediaTiempoCSP))
    print("Porcentaje de mejora " + str((mediaTiempoDist/mediaTiempoStar)*100)+"%")

    print("Media tiempo BFS " + str(mediaTiempoBfs * 1000) + " ms")
    print("Media tiempo Star " + str(mediaTiempoStar * 1000) + " ms")
    print("Media tiempo Disk " + str(mediaTiempoDist * 1000) + " ms")
    print("Porcentaje de mejora Astar " + str((mediaTiempoDist / mediaTiempoStar) * 100) + "%")
    print("Porcentaje de mejora BFS " + str((mediaTiempoDist / mediaTiempoBfs) * 100) + "%")
