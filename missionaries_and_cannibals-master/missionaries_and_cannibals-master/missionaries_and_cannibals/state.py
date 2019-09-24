import operator

class State :
    def __init__(self, state, action):
        self.state = state
        self.action = action

    def move(self):
        if self.action[2] == 1:
            self.state[0] += self.action[0]
            self.state[1] += self.action[1]
            self.state[2] = 0
        elif self.action[2] == 0:
            self.state[0] -= self.action[0]
            self.state[1] -= self.action[0]
            self.state[2] = 1
        return self.state    

    def isActionValid(self):
        if self.isSamestate():
            return True
        elif self.isSafeLeftMissionaries():
            return True
        elif self.isSafeRightMissionaries():
            return True
        else:
            return False
        
    def isSamestate(self):
        if self.state[2] == self.action[2]:
            return True
        else:
            return False

    def isSafeLeftMissionaries(self):
        if self.state[0] == 0:
            return True
        elif self.state[0] >= self.state[1]:
            return True
        else:
            return False

    def isSafeRightMissionaries(self):
        if self.state[0] == 0:
            return True
        elif self.state [0] >= self.state[1]:
            return True
        else:
            return False

