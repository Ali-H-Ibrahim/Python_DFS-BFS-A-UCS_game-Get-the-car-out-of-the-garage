# This is a sample Python script.

import states as ss
import cars as c
import cells as s
import LogicGameCar

#------------------------------ initalizing -------------------------------------#
n = 5
m = 7
a = [['-'] * m for i in range(n)]

numCar = 13
car = [-1 for i in range(numCar)]
stat = 0

#************************** level_1 **************************************

car[0] = c.Cars([s.cells(2, 0), s.cells(2, 1), s.cells(2, 2)], 'H', 'x',1)
car[1] = c.Cars([s.cells(4, 2), s.cells(4, 3)], 'H', 4,1)
car[2] = c.Cars([s.cells(2, 3), s.cells(3, 3)], 'A', 3,1)
car[3] = c.Cars([s.cells(0, 5), s.cells(0, 6)], 'H', 9,1)
car[4] = c.Cars([s.cells(1, 6), s.cells(2, 6)], 'A', 7,1)
car[5] = c.Cars([s.cells(2, 5), s.cells(3, 5)], 'A', 5,1)

car[9] = c.Cars([s.cells(0, 0), s.cells(1, 0)], 'A', 1,1)
car[7] = c.Cars([s.cells(3, 0), s.cells(4, 0)], 'A', 2,1)
car[6] = c.Cars([s.cells(3, 6), s.cells(4, 6)], 'A', 6,1 )
car[8] = c.Cars([s.cells(0, 1), s.cells(0, 2)], 'H', 8,1)
car[10] = c.Cars([s.cells(1, 2), s.cells(1, 3)], 'H', 10,1)
car[11] = c.Cars([s.cells(3, 1), s.cells(3, 2)], 'H', 11,1)
car[12] = c.Cars([s.cells(4, 4), s.cells(4, 5)], 'H', 12,1)


#************************** level_2 **************************************

# car[0] = c.Cars([s.cells(2, 0), s.cells(2, 1), s.cells(2, 2)], 'H', 'x',1)
# car[1] = c.Cars([s.cells(0, 0), s.cells(1, 0)], 'A', 1,1)
# car[2] = c.Cars([s.cells(3, 0), s.cells(4, 0)], 'A', 2,1)
# car[3] = c.Cars([s.cells(2, 3), s.cells(3, 3)], 'A', 3,1)
# car[4] = c.Cars([s.cells(4, 2), s.cells(4, 3)], 'H', 4,1)
# car[5] = c.Cars([s.cells(2, 4), s.cells(3, 4)], 'A', 5,1)
# car[6] = c.Cars([s.cells(3, 6), s.cells(4, 6)], 'A', 6,1 )
# car[7] = c.Cars([s.cells(1, 6), s.cells(2, 6)], 'A', 7,1)
# car[8] = c.Cars([s.cells(0, 3), s.cells(0, 4)], 'H', 8,1)
# car[9] = c.Cars([s.cells(0, 5), s.cells(0, 6)], 'H', 9,1)
# car[10] = c.Cars([s.cells(1, 2), s.cells(1, 3)], 'H', 10,1)
# car[11] = c.Cars([s.cells(3, 1), s.cells(3, 2)], 'H', 11,1)
# car[12] = c.Cars([s.cells(4, 4), s.cells(4, 5)], 'H', 12,1)


bs = ss.States(a, car, None, 0)
bs.begin_Status()
G = LogicGameCar.Game(bs)
bs.print_gride()


#------------------------------ UCS -------------------------------------#

G.ucs(bs)
G.path(G.goul)


#------------------------------ A* -------------------------------------#


# G.a_star(bs)
# G.path(G.goul)