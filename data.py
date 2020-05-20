import numpy
import time

from AStar import AStar
from Cities import C
from Dijkstra import Dijkstra
from csp import CSP

if __name__ == '__main__':
    matrix = numpy.loadtxt(open("data.csv", "rb"), delimiter=",", skiprows=1, dtype=int)

    rightTimes = 0
    totalCases = 0
    totalTimeStar = 0
    totalTimeDist = 0
    astar = AStar(matrix)
    disktra = Dijkstra(matrix)
    csp = CSP(matrix)
    (costAstar, path, timeAStar) = csp.resolve(C.HOSPITALET, C.MURCIA)
    print(path)
    for city in C:
        for city2 in C:

            print("From :" + city.name + "\t" "to :" + city2.name)
            (costAstar, pathAStar, timeAStar) = astar.resolve(city, city2)
            print("Astart GOT: " + "Cost of:" + str(costAstar) + " Path of: " + str(pathAStar) + " Time of: " + str(
                timeAStar))
            (costDisk, pathDisk, timeDisk) = disktra.resolve(city, city2)
            print(
                "Disk GOT: " + "Cost of:" + str(costDisk) + " Path of: " + str(pathDisk) + " Time of: " + str(timeDisk))

            totalTimeDist += timeDisk
            totalTimeStar += timeAStar
            if pathAStar == pathDisk:
                rightTimes += 1
            totalCases += 1

    print("Total Cases " + str(totalCases))
    print("Right Cases " + str(rightTimes))
    print("Right Percentaje " + str((rightTimes / totalCases) * 100)+"%")

    mediaTiempoStar = totalTimeStar / totalCases
    mediaTiempoDist = totalTimeDist / totalCases
    print("Media tiempo Star " + str(mediaTiempoStar))
    print("Media tiempo Disk " + str(mediaTiempoDist))
    print("Porcentaje de mejora " + str((mediaTiempoDist/mediaTiempoStar)*100)+"%")

