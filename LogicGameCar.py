#########################################################################################


#                                   Logic                                               #

#########################################################################################

import sys

sys.setrecursionlimit(4000)


class Game:
    visited_states = []
    queue = []
    goul = None

    def __init__(self, bs):

        self.bs = bs
        self.l = []
        self.sul = 0
        self.cont = 0
        self.last_car = 0

    def eqal(self, b1, b2):
        if b1 == b2:
            return True
        else:
            return False

    # ****************************DFS*******************************

    def dfs(self, state):

        if state in self.visited_states:
            # print('ww')
            del state
            return 0

        if state.gool():
            print(self.cont)
            print('--won--')
            self.goul = state
            state.print_gride()
            return 1

        self.visited_states.append(state)
        next_state = state.next_states()
        self.cont += 1
        for ch_state in next_state:
            if self.dfs(ch_state) == 1:

                return 1

    # ****************************BFS*******************************

    def bfs(self, state):
        print('********BFS*********')

        self.visited_states.append(state)
        self.queue.append(state)
        self.cont += 1
        while len(self.queue) > 0:

            self.cont += 1
            node = self.queue.pop(0)

            if node.gool():
                node.print_gride()
                self.goul = node
                print(self.cont)
                break

            next_state = node.next_states()

            for ch_state in next_state:

                if ch_state in self.visited_states:
                    continue

                else:

                    self.visited_states.append(ch_state)
                    self.queue.append(ch_state)

    # ****************************UCS*******************************
    def ucs(self, state):

        print('*********UCS*********')
        self.visited_states.append(state)
        self.queue.append(state)
        self.cont += 1
        # queue
        while len(self.queue) > 0:
            self.cont += 1
            node = self.pop()
            print(self.cont)
            if node.gool():
                node.print_gride()
                self.goul = node
                print(self.cont)
                print(node.cost)
                break
            next_state = node.next_states()
            for ch_state in next_state:
                if ch_state in self.visited_states:
                    continue
                else:
                    self.visited_states.append(ch_state)
                    self.queue.append(ch_state)

    # ***************************  (A*)    *******************************

    def a_star(self, state):

        print('*********A_star*********')
        self.visited_states.append(state)
        self.queue.append(state)
        self.cont += 1
        # queue
        while len(self.queue) > 0:
            self.cont += 1
            node = self.popstar()
            print(self.cont)
            if node.gool():
                node.print_gride()
                self.goul = node
                print(self.cont)
                print(node.cost)
                break
            next_state = node.next_states()
            for ch_state in next_state:
                if ch_state in self.visited_states:
                    continue
                else:
                    self.visited_states.append(ch_state)
                    self.queue.append(ch_state)

    def path(self, state):
        # ------- print path -------------
        c = 0
        l = []

        print(f'Cost of success :{state.cost}')
        print('#path_solution')
        while state.parent:
            l.append(state)
            state = state.parent
            c += 1

        for i in range(len(l)):
            print(f"#State_{i + 1}")
            l.pop().print_gride()

        print(f"Cost of path {c}")

    def pop(self):
        # ------- pop in UCS -------------

        c = 0
        r = 0
        for n, i in enumerate(self.queue):
            if c == 0:
                c = i
                r = n
            elif c.cost > i.cost:
                c = i
                r = n
        return self.queue.pop(r)






    def h_f(self, state):
        # ------- تابع التجريبية  -------------

        l = []
        # ************************** Step_1 **************************
        c = 6 - state.car[0].Xpos[2].j

        # ************************** Step_2 *************************
        for i in range(7):
            if i > state.car[0].Xpos[2].j:
                if state.gride[2][i] != '-':
                    l.append(state.gride[2][i])

                    c = c + 1
        # ************************** Step_3 ***********************
        for i in l:
            if state.can_move(state.car[i], 'U'):
                pass
            elif state.can_move(state.car[i], 'D'):
                pass
            else:
                c = c + 1
        return c


    def popstar(self):

        # ------- pop in (A*) -------------
        c = 0
        r = 0
        for n, i in enumerate(self.queue):
            if c == 0:
                c = i
                r = n
            elif c.cost + self.h_f(c) > i.cost + self.h_f(i):
                c = i
                r = n
        return self.queue.pop(r)
