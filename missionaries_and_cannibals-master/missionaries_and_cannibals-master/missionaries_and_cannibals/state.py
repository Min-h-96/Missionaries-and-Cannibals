import operator

class State :
    def __init__(self, state, action):
        self.state = state
        self.action = action

    def move(self) :
        pass

    def isActionValid(self) :
        pass
        
