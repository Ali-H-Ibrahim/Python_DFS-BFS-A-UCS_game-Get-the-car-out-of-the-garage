#########################################################################################


#                                   States                                              #

#########################################################################################


import copy
from termcolor import colored


class States:
    n = 5
    m = 7

    def __init__(self, gride, car, parent, cost):
        self.gride = gride
        self.car = car
        self.parent = parent
        self.cost = cost


    def gool(self):
        return self.gride[2][6] == 'x'


    def __eq__(self, other):
        if hasattr(self, 'gride'):
            if hasattr(other, 'gride'):
                return self.gride == other.gride
            return False
        return True


    def begin_Status(self):
        # car X
        for ii in self.car:
            for n, c in enumerate(ii.Xpos):
                self.gride[ii.Xpos[n].i][ii.Xpos[n].j] = ii.id




    def can_move(self, c, d):

        if c.id == 'x':
            if d == 'R':
                return c.Xpos[2].j + 1 < self.m and self.gride[c.Xpos[2].i][c.Xpos[2].j + 1] == '-'

            if d == 'L':
                return c.Xpos[0].j - 1 >= 0 and self.gride[c.Xpos[0].i][c.Xpos[0].j - 1] == '-'

            else:
                return False


        elif c.direction == 'A':
            if d == 'U':
                return c.Xpos[0].i - 1 >= 0 and self.gride[c.Xpos[0].i - 1][c.Xpos[0].j] == '-'

            if d == 'D':
                return c.Xpos[1].i + 1 < self.n and self.gride[c.Xpos[1].i + 1][c.Xpos[1].j] == '-'
            else:

                return False
        else:
            if d == 'R':
                return c.Xpos[1].j + 1 < self.m and self.gride[c.Xpos[1].i][c.Xpos[1].j + 1] == '-'

            if d == 'L':
                return c.Xpos[0].j - 1 >= 0 and self.gride[c.Xpos[0].i][c.Xpos[0].j - 1] == '-'

            else:
                return False

    def move(self, c, d):

        for n, ce in enumerate(c.Xpos):
            self.gride[c.Xpos[n].i][c.Xpos[n].j] = '-'
            if d == 'R':
                c.Xpos[n].j += 1
            elif d == 'L':
                c.Xpos[n].j -= 1
            elif d == 'U':
                c.Xpos[n].i -= 1
            elif d == 'D':
                c.Xpos[n].i += 1

        self.begin_Status()





    def next_states(self):
        l = []

        for i, c in enumerate(self.car):

            if c.direction == 'H':

                if self.can_move(c, 'L'):
                    newS = copy.deepcopy(self)

                    newS.move(newS.car[i], 'L')
                    newS.parent = self
                    newS.cost = self.cost + c.w
                    # newS.car.clear()
                    l.append(newS)

                if self.can_move(c, 'R'):
                    newS = copy.deepcopy(self)
                    newS.cost = self.cost + c.w
                    newS.parent = self
                    newS.move(newS.car[i], 'R')
                    # newS.car.clear()
                    l.append(newS)

            else:

                if self.can_move(c, 'U'):
                    newS = copy.deepcopy(self)
                    # newS = self.clone()
                    newS.parent = self
                    newS.cost = self.cost + c.w

                    newS.move(newS.car[i], 'U')
                    l.append(newS)

                if self.can_move(c, 'D'):
                    newS = copy.deepcopy(self)
                    newS.parent = self
                    newS.cost = self.cost + c.w
                    newS.move(newS.car[i], 'D')

                    # newS.car.clear()
                    l.append(newS)

        return l




    def print_gride(self):
        print(colored('*' * 38), end="")
        for n, i in enumerate(self.gride):
            print('')

            for j in i:

                if j == 'x':
                    print(colored("{:^5}".format(j), 'red'), end='')

                elif j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    print(colored("{:^5}".format(j), 'green'), end='')

                else:
                    print("{:^5}".format(j), end='')
            if n == 2:
                print(colored('    Exit', 'yellow'), end='')
            else:
                print('||', end='')

        print()
        print(colored('*' * 38))


