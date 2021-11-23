# Image performing

# Description: program creates and saves image in different formats
# from dots with coordinates that are picked up in text file (dataset)

# Done by Denys Dolynniy
# Date: 15.10.2021

import numpy as np
from matplotlib import pyplot as plt

# class for reading and editing text file (dataset)
class Readfile:

    #function for opening and reading file
    def readFile():
        with open("DS3.txt") as f:
            lines = f.readlines()
        f.close()
        return lines

    #funcion for editing dataset
    def editLines(readFile):
        unformed_coordinates = []
        for line in readFile():
            unformed_coordinates.append(list(line))
    
        arr = list()

        for dot in unformed_coordinates:
            for num in range(len(dot)):
                if dot[num] == '\n':
                    dot.remove(dot[num])
            r1 = []
            r2 = []
            r = []
            for num in range(len(dot)):
                if dot[num] == ' ':
                    r1 = dot[0:num]
                    r2 = dot[num + 1:len(dot)]
                    r = [r1, r2]
                    arr.append(r)

        coordinates = []
        for dot in arr:
            dot_1 = []
            for axis in dot:
                l = ''
                for k in range(len(axis)):
                    l = l + axis[k]
                axis = int(l)
                dot_1.append(axis)
            coordinates.append(dot_1)

        coordinates = np.array(coordinates)

        return coordinates

    coordinates = editLines(readFile)

dots = Readfile()
coordinates = dots.coordinates

# class for displaying coorditanes with certain canvas size of window
# and saving image in any graphical format
class Performdots:

    x, y = coordinates.T
    
    px = 1 / plt.rcParams['figure.dpi']
    plt.subplots(figsize=(960 * px, 540 * px))

    plt.scatter(x, y)

    gra_format = 'png'
    plt.savefig(f'Figure.{gra_format}', dpi=200)
    plt.show()


