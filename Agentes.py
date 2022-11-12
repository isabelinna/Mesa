import mesa
import matplotlib.pyplot as plt
 
def compute_bot(model):
        counter = 0
        for agent in model.schedule.agents:
           # print(agent.type)
            if agent.type ==3: 
                counter = counter + 1
                print("Contador:",counter)
        return counter       
    
    
class Basura(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.type = 1
        


class Bot(mesa.Agent):
    

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)

        if self.model.grid.is_cell_empty(new_position):
            self.model.grid.move_agent(self, new_position)
        else:     
            if self.model.grid[new_position][0].type == 1:
                    self.model.grid[new_position][0].type = 3    
                    self.model.grid.move_agent(self, new_position)

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.type = 0
    
    

    def step(self):
        self.move()

    

        


