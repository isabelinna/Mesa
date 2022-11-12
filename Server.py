import mesa
from Model import *
from mesa.visualization.UserParam import UserSettableParameter

parametros = {
    "agentes": UserSettableParameter(
        "slider",
        "Number of agents",
        5,     # Default
        1,      #Min
        100,    #Max
        1,       #Step
        description="Cuantos Bots spawnean",
    ), "N": 10, "M": 10,

    "tiempoMax": UserSettableParameter(
        "number",
        "Max steps",
        value=100,
        description="Choose how many steps you want",
    ),

    "porcentaje": UserSettableParameter(
        "slider",
        "Floor Covered in dirt",
        15,        # Default
        1,        #Min
        90,          #Max
        1,        #Step
        description="Porcentaje del grid con basura",
    )
        
}
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

chart = mesa.visualization.ChartModule([{"Label": "Basura recogida",
                     "Color": "Purple"}],
                  data_collector_name='datacollector')

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    CleanerBot, [grid,chart], "Robot Limpieza", parametros)





server.port = 8521  # The default
server.launch()