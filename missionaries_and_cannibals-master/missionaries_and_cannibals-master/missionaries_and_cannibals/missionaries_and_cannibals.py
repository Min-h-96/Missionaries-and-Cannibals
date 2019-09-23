from search import Problem
from .state import State

class MissionariesAndCannibals(Problem) :
    def __init__(self, initial, goal):
        self.initial = initial
        print('initial state is...')
        print(initial)
        self.goal = goal
    
    def getActions(self) :
        return {
            (1, 0, 0),
            (2, 0, 0),
            (0, 1, 0),
            (0, 2, 0),
            (1, 1, 0),
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)     
        }

    def actions(self, state) :
        return self.getValidAction(state, self.getActions())


    def result(self, state, action) :
        state = State(state, action)
        return state.move()

    def getValidAction(self, state, allActions) :
        pass
    
    def goal_test(self, state) :
        return state == self.goal
