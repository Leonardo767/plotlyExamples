# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:27:55 2018

@author: Leonardo
"""

# --------------------------------------------------------
# IMPORTS:
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
# --------------------------------------------------------
# --------------------------------------------------------
# FUNCTIONS:
def unpackXYZcoords(A):
    x = [0]*A.shape[0]**2  # empty preallocation
    y = [0]*A.shape[0]**2  # empty preallocation
    z = [0]*A.shape[0]**2  # empty preallocation
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            x[i*A.shape[1] + j] = i
            y[i*A.shape[1] + j] = j
            z[i*A.shape[1] + j] = A[i][j]
    return x,y,z
# --------------------------------------------------------


# Build A, which stores x,y values as index, and z as value
dim = 10
A = np.zeros((dim, dim))

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i][j] = i*j
print(A)

# unpack x, y, and z
x1,y1,z1 = unpackXYZcoords(A)

# build plot
trace1 = go.Scatter3d(
    x=x1,
    y=y1,
    z=z1,
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
