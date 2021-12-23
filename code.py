import plotly.express as px
import pandas as pd


df = pd.read_csv("savings_data.csv")
fig = px.bar(df, y = "quant_saved", color = "rem_any")
fig.show()