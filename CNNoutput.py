# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:52:55 2018

@author: Leonardo
"""

from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np


f = 5
p = 2
s = 1
dud = np.ones((1,101))
n = np.linspace(0,1000,101)
Size = (n + 2*p - f)//s + 1

# ratio of n_output/n_input
Expansion = Size/n

x = list(dud.T)
y = list(n)
z = list(2*n + 20)

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        line=dict(
            color='rgba(217, 217, 217, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)


plot(fig)
 

