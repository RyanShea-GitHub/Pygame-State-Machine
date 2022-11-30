class State():
    def __init__(self, game):
        self.game = game
        self.prev_State = None

    def update(self, delta_Time, user_Actions):
        pass

    def render(self, surface):
        pass

    def enter_State(self):
        if len(self.game.state_Stack) > 1:
            self.prev_State = self.game.state_Stack[-1]
        self.game.state_Stack.append(self)

    def exit_State(self):
        self.game.state_Stack.pop()
