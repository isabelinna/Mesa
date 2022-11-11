import mesa
from Model import *

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

chart = mesa.visualization.ChartModule([{"Label": "Gini",
                     "Color": "Black"}],
                  data_collector_name='datacollector')

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    CleanerBot, [grid,chart], "Robot Limpieza", {"agentes": 5, "N": 10, "M": 10, "tiempoMax": 100, "porcentaje": 15}
)




server.port = 8521  # The default
server.launch()