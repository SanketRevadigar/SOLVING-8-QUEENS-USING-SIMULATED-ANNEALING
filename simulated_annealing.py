# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:08:33 2021

@author: Sanket Revadigar
"""


import random, math
import decimal
#from copy import deepcopy, copy
from datetime import datetime

#initalise the 8 queens problem randomly
class Initial_state:
    def __init__(self, total_queens=8):
        self.total_queens = total_queens
        self.reset_board()
    #fucntion to reset the board
    def reset_board(self):
        self.queens = [-1 for i in range(0, self.total_queens)]

        for i in range(0, self.total_queens):
            self.queens[i] = random.randint(0, self.total_queens - 1)
            # self.queens[row] = column

    #calculates the cost
    def cost_value(self):
        attack = 0

        for queen in range(0, self.total_queens):
            for queen_next in range(queen+1, self.total_queens):
                if self.queens[queen] == self.queens[queen_next] or abs(queen - queen_next) == abs(self.queens[queen] - self.queens[queen_next]):
                    attack += 1

        return attack

    @staticmethod
    def cost_value_queen(queens):
        attack = 0
        total_queens = len(queens)

        for queen in range(0, total_queens):
            for queen_next in range(queen+1, total_queens):
                if queens[queen] == queens[queen_next] or abs(queen - queen_next) == abs(queens[queen] - queens[queen_next]):
                    attack += 1

        return attack

    @staticmethod
    def to_string(queens):
        board_To_string = ""

        for row, column in enumerate(queens):
            board_To_string += "(%s, %s)\n\n" % (row, column)

        return board_To_string
    #calculate the lowest value of the state
    def lowest_value_state(self):
        #disp_count = 0
        temporary_queens = self.queens
       #lowest_cost = self.cost_value(temporary_queens)

        for i in range(0, self.total_queens):
            temporary_queens[i] = (temporary_queens[i] + 1) % (self.total_queens - 1)

            for j in range(self.total_queens):
                temporary_queens[j] = (temporary_queens[j] + 1) % (self.total_queens - 1)

    def __str__(self):
        board_To_string = ""

        for row, column in enumerate(self.queens):
            board_To_string += "(%s, %s)\n\n" % (row, column)

        return board_To_string

class simulated_annealing:
    def __init__(self, state):
        self.timespent = 0;
        self.state = state
        self.temperature = 4000
        self.sch = 0.99
        self.start_time = datetime.now()


    def start(self):
        state = self.state
        board_queens = self.state.queens[:]
        solution = False

        for k in range(0, 170000):
            self.temperature *= self.sch
            state.reset_board()
            successor_queens = state.queens[:]
            dw = Initial_state.cost_value_queen(successor_queens) - Initial_state.cost_value_queen(board_queens)
            exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(self.temperature)))

            if dw > 0 or random.uniform(0, 1) < exp:
                board_queens = successor_queens[:]

            if Initial_state.cost_value_queen(board_queens) == 0:
                print("Goal_state:")
                print(Initial_state.to_string(board_queens))
                self.timespent = self.time_spent()
                print("Successful\nTime Spent : %sms" % (str(self.timespent)))
                solution = True
                break

        if solution == False:
            self.timespent = self.time_spent()
            print("Unsuccessful\nTime Spent : %sms" % (str(self.timespent)))

        return self.timespent

    def time_spent(self):
        end_time = datetime.now()
        timespent = (end_time - self.start_time).microseconds / 1000
        return timespent


if __name__ == '__main__':
    state = Initial_state()
    print("Initial_state:")
    print(state)
    simulated_annealing(state).start()