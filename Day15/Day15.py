import re

sensors = set()
beacons = set()

data = open('input.txt').read().strip()
for line in data.split('\n'):
    coords = re.findall("(-?\d+)", line)
    coords = [int(i) for i in coords]
    sc, sr = coords[0], coords[1]
    bc, br = coords[2], coords[3]
    d = abs(sr-br) + abs(sc-bc)
    beacons.add((bc, br))
    sensors.add((sc, sr, d))

def possible_beacon(c, r):
    for sc, sr, d in sensors:
        if abs(c - sc) + abs(r - sr) <= d and (c, r) not in beacons:
            return False
    return True

def p1(row):

    no_beacon = set()

    for sc, sr, d in sensors:
        dr = abs(row - sr) #how far away vertically the target line is from current signal
        dc = d-dr #how many horizonal positions on the target line

        if dc >= 0:
            for i in range(-dc, dc+1):
                pos = (sc+i, row)
                if pos not in beacons:
                    no_beacon.add(pos)
    
    return print(len(no_beacon))

def p2(max):

    offsets = [(-1, 1), (1, -1), (-1, -1), (1, 1)] #diagonals

    for sc, sr, d in sensors:
        for dc in range(d+2):
            dr = (d+1) - dc
            for co, ro in offsets:
                c = sc + (dc * co)
                r = sr + (dr * ro)
                #c,r is all points on outside perimeter of the signal
                #where another beacon could be
                if 0<=c<=max and 0<=r<=max and (c,r) not in beacons:
                    if possible_beacon(c,r):
                        return print(c * 4000000 + r)
    
    


p1(2000000)
p2(4000000)
