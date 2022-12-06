import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

fig = go.Figure()
x = np.arange(-10.5, 10.5, 0.05)
f = 5*x**2+10*x - 30    

fig.add_trace(go.Scatter(x=x, y=f,mode='lines+markers', name='$$f(x)=x^2$$'))
fig.update_layout(legend_orientation="h",
                  legend=dict(x=.05, xanchor="center"),
                  margin=dict(l=0, r=0, t=0, b=0))

fig.show()