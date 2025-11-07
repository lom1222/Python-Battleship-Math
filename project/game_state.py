


class GameState:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = self.create_base_game_state(width, height)


    def create_base_game_state(self, width, height):
        state = []
        for x in range(width):
            state.append([])
            for y in range(height):
                state[x].append(Cell(x,y,"unknown"))

        return state

    def cell(self,x,y):
        return self.state[x][y]

    def get_debug(self, type):
        debug = ""
        if type == "basic":
            debug += "\nDebug type - Basic\n______\n "
            for column in range(self.width):
                debug += " "+str(column)+" "
            for row in range(self.width):
                debug += "\n"+str(row)
                for cell in self.state[row]:
                    debug += "["+cell.state[0]+"]"
            debug += "\n-----\n"
        elif type == "verbose":
            debug += "Debug type - Verbose\n______\n"
        return debug


class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.probability = 0

    def get_debug(self, type):
        if type == "basic":
            return "Cell: ("+str(self.x)+", "+str(self.y)+")"
        elif type == "verbose":
            return "Cell: ("+str(self.x)+", "+str(self.y)+") - State: "+str(self.state)+" - Probability: "+str(self.probability)
        else:
            return 0