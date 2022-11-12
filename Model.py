import mesa
from Agentes import *

class CleanerBot(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, agentes, N, M, tiempoMax, porcentaje):
        self.percent = porcentaje
        self.num_agents = agentes
        self.tiempo = tiempoMax
        self.grid = mesa.space.MultiGrid(N, M, False)
        self.schedule = mesa.time.RandomActivation(self) 
        self.running = True
        self.current_step= 1

        # Create agents
        for i in range(self.num_agents):
            a = Bot(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = 1
            y = 1
            self.grid.place_agent(a, (x, y))
        cellPercent= int(porcentaje/100 *(N*M))
        for i in range(cellPercent):
            # Add the agent to a random grid cell

            x = self.random.randrange(self.grid.height)
            y = self.random.randrange(self.grid.width) 
            if self.grid.is_cell_empty((x,y)):
                a = Basura((x,y), self) 
                self.schedule.add(a)

                self.grid.place_agent(a, (x, y))
                

        self.datacollector = mesa.DataCollector(
            model_reporters={"Basura recogida": compute_bot} 
                  
        )



    def step(self):
        
        if self.current_step <= self.tiempo:
            self.schedule.step()
            self.current_step += 1
            self.datacollector.collect(self)
        else:
            
            self.running = False
    
 
            

           
