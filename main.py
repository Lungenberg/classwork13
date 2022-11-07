import csv
import os
import random
def afisa(file):
    f = open(file, 'r')
    x = csv.reader(f)
    karta = []
    for line in x:
        karta.append(line)
    return karta

def krasivo(m, map):
    m2 = m[:]
    os.system('clean')
    draw = " "
    for row in m2:
        for i in row:
            i = str(i).replace("1", "██")
            i = str(i).replace("0", "  ")
            draw += i
        draw +="\n"
    print(draw)

def move(pers):
    krasivo(labirint, [])
    a = pers[-1]
    possibility = [(a[0], a[1]+1), (a[0], a[1]-1), (a[0]+1, a[1]), (a[0]-1, a[1])]
    random.shuffle(possibility)
    for item in possibility:
        if item[0] < 0 or item[1] < 0 or item[0] > len[labirint] or


labirint = afisa('maze.csv')
krasivo(labirint, [])
print(labirint)