
class Order:
    def __init__(self, instruction, *params):
        self.instruction = bytes(instruction)
        self.params = []

        for param in params:
            self.params.insert(0, param)