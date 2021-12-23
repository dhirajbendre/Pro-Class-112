import pandas as pd
import statistics
import plotly.express as px


#Plotting the graph
df = pd.read_csv("savings_data.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()
