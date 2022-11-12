import mesa
from Agentes import *

# Archivo para definir la clase CleanerBot, modelo de los robots de limpieza
# Autores: Isabel Vieyra A01745860 Germán Guzmán A01752165
# Creación: 09/11/22 -> modificación 11/11/22

# Modelo de los robots de limpieza, crea y añade los agentes a la simulación

class CleanerBot(mesa.Model):

    def __init__(self, agentes, N, M, tiempoMax, porcentaje):
        self.percent = porcentaje
        self.num_agents = agentes
        self.tiempo = tiempoMax
        self.grid = mesa.space.MultiGrid(N, M, False)
        self.schedule = mesa.time.RandomActivation(self) 
        self.running = True
        self.current_step= 1

        # Crear agentes
        
        for i in range(self.num_agents):
            a = Bot(i, self)
            self.schedule.add(a)
            # Añadirlos a una celda al azar
            x = 1
            y = 1
            self.grid.place_agent(a, (x, y))
        cellPercent= int(porcentaje/100 *(N*M))
        for i in range(cellPercent):
            # Añadir los agentes basura

            x = self.random.randrange(self.grid.height)
            y = self.random.randrange(self.grid.width) 
            if self.grid.is_cell_empty((x,y)):
                a = Basura((x,y), self) 
                self.schedule.add(a)

                self.grid.place_agent(a, (x, y))
                
        # Utilizar DataCollector para graficar la función compute_bot
        
        self.datacollector = mesa.DataCollector(
            model_reporters={"Basura recogida": compute_bot} 
                  
        )

    # Función step que se detiene cuando el tiempoMax(steps) se termina

    def step(self):
        
        if self.current_step <= self.tiempo:
            self.schedule.step()
            self.current_step += 1
            self.datacollector.collect(self)
        else:
            
            self.running = False
    
 
            

           
