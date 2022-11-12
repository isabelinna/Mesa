import mesa

# Archivo que contiene los agentes utilizados en la simulación
# Autores: Isabel Vieyra A01745860, Germán Guzmán A01752165
# Creación de archivo: 09/11/22 -> modificación: 11/11/22
 
# Función utilizada para graficar la cantidad de basuras recogidas por steps 
# acepta modelo como argumento y regresa el contador de steps

def compute_bot(model):
 
        counter = 0
        for agent in model.schedule.agents:
           # print(agent.type)
            if agent.type ==3: 
                counter = counter + 1
                print("Contador:",counter)
        return counter       
    
# Clase Basura, en esta definimos al agente basura, se utiliza type=1 para distinguirlo de otros agentes
    
class Basura(mesa.Agent):
 
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.type = 1
        

# Clase Bot, se define al agente robot el cual recogerá basura
      
class Bot(mesa.Agent):
    
# Función que plasma al bot en una celda vecina aleatoria mientras no haya otro bot ahí

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
             
    # Función para definir al agente, se le asigna type = 0
             
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.type = 0
    
    

    def step(self):
        self.move()

    

        


