import numpy as np
import sys

'''

        Z
        |
        |
        |
        +-----------Y
       /
      /
    X


    Cube centered in coordinate system (X,Y,Z) = (0,0,0)

                                White "UP"      (0,0,1)

    Black  "LEFT" (0,-1,0)      Green "FRONT"   (1,0,0)         Blue "RIGHT"    (0,1,0)

                                Purple "DOWN"   (0,0,-1)

                                Orange  "BACK"  (-1,0,0)

Class CubeRotation
    states
        frontside
        upside

    .rotate(LEFT/RIGHT/UP/DOWN)
    .color(FRONT/BACK/LEFT/RIGHT/UP/DOWN)
    .print

'''

class CubeRotation:

    def __init__(self):
        self.front = np.array([1, 0, 0])   # "Green"
        self.up = np.array([0, 0, 1])      # "White"

    def vector2color(self, v):
        if np.array_equal(v, [0, 0, 1]):
                return "WHITE"
        if np.array_equal(v, [1, 0, 0]):
                return "GREEN"
        if np.array_equal(v, [0, -1, 0]):
                return "BLACK"
        if np.array_equal(v, [0, 1, 0]):
                return "BLUE"
        if np.array_equal(v, [0, 0, -1]):
                return "PURPLE"
        if np.array_equal(v, [-1, 0, 0]):
                return "ORANGE"
        print "ERROR - illegal vector"
        sys.exit(1)

    def printColor(self, color):
        if color == "GREEN":
            return '\033[42m'
        if color == "WHITE":
            return '\033[40m'
        if color == "BLACK":
            return '\033[48m'
        if color == "PURPLE":
            return '\033[45m'
        if color == "BLUE":
            return '\033[44m'
        if color == "ORANGE":
            return '\033[43m'
        if color == "NORMAL":
            return '\033[0m'
        if color == "OTHER":
            return '\033[41m'

        print "ERROR - illegal color"
        sys.exit(1)

    def printSide(self, color):
        if color=="OTHER":
            sys.stdout.write(self.printColor(color) + '+++' + self.printColor('NORMAL'))
        else:
            sys.stdout.write(self.printColor(color) + '   ' + self.printColor('NORMAL'))

    def side2color(self, side):
        if side == "UP":
            return self.vector2color(self.up)
        if side == "DOWN":
            return self.vector2color(-1*self.up)
        if side == "LEFT":
            return self.vector2color(-1*np.cross(self.up, self.front))
        if side == "RIGHT":
            return self.vector2color(np.cross(self.up, self.front))
        if side == "FRONT":
            return self.vector2color(self.front)
        if side == "BACK":
            return self.vector2color(-1*self.front)

        print "ERROR - illegal side"
        sys.exit(1)

    def printCube(self):
        '''
            print background + UP + background
        '''
        self.printSide('OTHER')
        self.printSide(self.side2color('UP'))
        self.printSide('OTHER')
        self.printSide('OTHER')
        print
        self.printSide(self.side2color('LEFT'))
        self.printSide(self.side2color('FRONT'))
        self.printSide(self.side2color('RIGHT'))
        self.printSide(self.side2color('BACK'))
        print
        self.printSide('OTHER')
        self.printSide(self.side2color('DOWN'))
        self.printSide('OTHER')
        self.printSide('OTHER')
        print

    def rotate(self, side):
        print side
        if side == "UP":
            tmp = self.front
            self.front = np.cross(np.cross(self.up, self.front), self.front)
            self.up = tmp
            return
        if side == "DOWN":
            tmp = self.up
            self.up = np.cross(self.up, np.cross(self.up, self.front))
            self.front = tmp
            return
        if side == "LEFT":
            self.front = -1 * np.cross(self.up, self.front)
            return
        if side == "RIGHT":
            self.front = np.cross(self.up, self.front)
            return

        print "ERROR - illegal side rot"
        sys.exit(1)

'''
loop
    print cube
    get keypress
    rotate
'''

print "Testing cube rotation, learning python..."
myCube = CubeRotation()

while True:
    print "up   : ",
    print myCube.up
    print "front: ",
    print myCube.front
    myCube.printCube()
    a = raw_input("rotate with a/w/s/d, q=quit :> ")
    print
    if a.strip() == 'q':
        break
    if a.strip() == 'a':
        myCube.rotate("LEFT")
    if a.strip() == 'w':
        myCube.rotate("UP")
    if a.strip() == 's':
        myCube.rotate("DOWN")
    if a.strip() == 'd':
        myCube.rotate("RIGHT")


# side2vector = {'UP': [0, 0, 1], 'FRONT': [1, 0, 0]}
