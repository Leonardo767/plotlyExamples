# -*- coding: utf-8 -*-
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



def findExpansion(f,s):
    # let's pass through a fixed input size of 10:
    n_In = 1000
    # same padding:
    p = f//2
    n_Out = (n_In + 2*p - f)//s + 1
    
    Expansion = n_Out/n_In
    
    return Expansion
    
# --------------------------------------------------------


f = np.linspace(1,100,100)
s = np.linspace(1,100,100)

A = np.zeros((len(f), len(s)))

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i][j] = findExpansion(f[i], s[j])  # store expansion based on filter and stride

#print(A)

"""
x, y, z = unpackXYZcoords(A)
trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=1,
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
"""

data = [
    go.Surface(
        z=A
    )
]
layout = go.Layout(
    title='CNN Output/Input Sizes',
    autosize=True,  # we want this to fill the screen
#    width=500,
#    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    ),
    xaxis=dict(
        title='Filter Size'
    ),
    yaxis=dict(
        title='Stride Length'
    )
)
fig = go.Figure(data=data, layout=layout)

plot(fig)
