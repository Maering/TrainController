# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:

class State:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

class LokState:
    def __init__(self, action):
        self.action = action
    def __cmp__(self, other):
        return self.action == other.action
    def __hash__(self):
        return hash(self.action)

LokState.init = LokState("init")
LokState.moving = LokState("moving")
LokState.stopped = LokState("stopped")