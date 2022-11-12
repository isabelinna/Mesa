import mesa
from Model import *
from mesa.visualization.UserParam import UserSettableParameter

# Archivo que contiene los parámetros, servidor y portrayal de la simulación
# Autores: Isabel Vieyra A01745860, Germán Guzmán A01752165
# Creación de archivo: 09/11/22 -> modificación: 11/11/22

# Parámetros del modelo CleanerBot

parametros = {
    "agentes": UserSettableParameter(
        "slider",
        "Número de agentes",
        5,     # Default
        1,      #Min
        100,    #Max
        1,       #Step
        description="Cuantos Bots desea",
    ), "N": 10, "M": 10,

    "tiempoMax": UserSettableParameter(
        "number",
        "Steps máximos",
        value=100,
        description="Cuántos steps se ejecutarán",
    ),

    "porcentaje": UserSettableParameter(
        "slider",
        "Porcentaje de basura",
        15,        # Default
        1,        #Min
        90,          #Max
        1,        #Step
        description="Porcentaje del grid con basura",
    )
        
}
# Portrayal de los agentes 

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.type == 1 :
        portrayal["Color"] = "black"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    elif agent.type == 3 :
        portrayal["Color"] = "white"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    else:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    return portrayal

# Visualización de la gráfica que mide los steps que tardan los robots en recoger basura

chart = mesa.visualization.ChartModule([{"Label": "Basura recogida",
                     "Color": "Purple"}],
                  data_collector_name='datacollector')

#Visualización de la cuadricula para la simulación

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    CleanerBot, [grid,chart], "Robot Limpieza", parametros)

# Creación del servidor en puerto default

server.port = 8521  # The default
server.launch()
