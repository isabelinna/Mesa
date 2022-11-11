from Agentes import *
import numpy as np
import pandas as pd
from Model import MoneyModel


#model = MoneyModel(50, 10, 10)
#for i in range(100):
#    model.step()
#gini = model.datacollector.get_model_vars_dataframe()
#gini.plot()



#params = {"width": 10, "height": 10, "N": range(10, 500, 10)}

#results = mesa.batch_run(
#    MoneyModel,
#    parameters=params,
#    iterations=5,
#    max_steps=100,
#    number_processes=1,
#    data_collection_period=1,
#    display_progress=True,
#)

#results_df = pd.DataFrame(results)

#results_filtered = results_df[(results_df.AgentID == 0) & (results_df.Step == 100)]
#N_values = results_filtered.N.values
#gini_values = results_filtered.Gini.values
#plt.scatter(N_values, gini_values)
#plt.show()


#plt.imshow(agent_counts, interpolation="nearest")
#plt.colorbar()
#plt.show()