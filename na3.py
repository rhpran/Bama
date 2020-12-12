# -*- coding: utf-8 -*-
"""NA3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fYyPEFkt2dpZslAjSHlOtWXxWbSHHt-B
"""

# Commented out IPython magic to ensure Python compatibility.
import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

G=[[]*1000]*1000
cnt=[[]*1000]*1000
cor=[[]*1000]*1000

G[1] = nx.petersen_graph()
G[2] = nx.davis_southern_women_graph()
G[3] = nx.florentine_families_graph()
G[4] = nx.les_miserables_graph()

cnt[1]=nx.closeness_centrality(G[2])
cnt[2]=nx.degree_centrality(G[2])
cnt[3]=nx.pagerank(G[2])

x=np.arange(1,len(cnt[1])+1,1)
x=cnt[1].values()
x=list(x)
x2=np.arange(1,len(cnt[3])+1,1)
x2=cnt[3].values()
x2=list(x2)
y=np.arange(1,len(cnt[2])+1,1)
y=cnt[2].values()
y=list(y)
plt.scatter(x=x,y=y)

from scipy import stats
beta, beta0, r_value, p_value, std_err = stats.linregress(x,y)
print("y = %f x + %f, r: %f, r-squared: %f,\np-value: %f, std_err: %f")
# % (beta, beta0, r_value, r_value**2, p_value, std_err))
# plotting the line
x = np.array(x)
yhat = beta * x + beta0 # regression line
plt.plot(x, yhat, 'r-', x, y,'o')
plt.xlabel('Closeness Centrality')
plt.ylabel('Degree Centrality')
plt.show()
y=np.array(y)
y=y.astype('float')
x2=np.array(x2)
import statsmodels.formula.api as smfrmla
# Build a model excluding the intercept, it is implicit
data={"x":pd.Series(x),"x2":pd.Series(x2),"y":pd.Series(y)}
df=pd.DataFrame(data)
model = smfrmla.ols('y ~ x + x2', df).fit()
print(model.summary())

df

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
plt.plot(x, sinus)
plt.show()
plt.plot(x, sinus, "o")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt
# %matplotlib inline
fvalues = np.linspace(.1, 5, 100)
# pdf(x, df1, df2): Probability density function at x of F.
plt.plot(fvalues, f.pdf(fvalues, 1, 30), 'b-', label="F(1, 30)")
plt.plot(fvalues, f.pdf(fvalues, 5, 30), 'r-', label="F(5, 30)")
plt.legend()
# cdf(x, df1, df2): Cumulative distribution function of F.
# ie.
proba_at_f_inf_3 = f.cdf(3, 1, 30) # P(F(1,30) < 3)
# ppf(q, df1, df2): Percent point function (inverse of cdf) at q of F.
f_at_proba_inf_95 = f.ppf(.95, 1, 30) # q such P(F(1,30) < .95)
assert f.cdf(f_at_proba_inf_95, 1, 30) == .95
# sf(x, df1, df2): Survival function (1 - cdf) at x of F.
proba_at_f_sup_3 = f.sf(3, 1, 30) # P(F(1,30) > 3)
assert proba_at_f_inf_3 + proba_at_f_sup_3 == 1
# p-value: P(F(1, 30)) < 0.05
low_proba_fvalues = fvalues[fvalues > f_at_proba_inf_95]
plt.fill_between(low_proba_fvalues, 0, f.pdf(low_proba_fvalues, 1, 30),
alpha=.8, label="P < 0.05")
plt.show()
      
spring_3D = nx.spring_layout(G[1],dim=3, seed=18)
x_nodes = [spring_3D[i][0] for i in range(len(G[1]))]# x-coordinates of nodes
y_nodes = [spring_3D[i][1] for i in range(len(G[1]))]# y-coordinates
z_nodes = [spring_3D[i][2] for i in range(len(G[1]))]# z-coordinates
edge_list = G[1].edges()
x_edges=[]
y_edges=[]
z_edges=[]

#need to fill these with all of the coordiates
for edge in edge_list:
    #format: [beginning,ending,None]
    x_coords = [spring_3D[edge[0]][0],spring_3D[edge[1]][0],None]
    x_edges += x_coords

    y_coords = [spring_3D[edge[0]][1],spring_3D[edge[1]][1],None]
    y_edges += y_coords

    z_coords = [spring_3D[edge[0]][2],spring_3D[edge[1]][2],None]
    z_edges += z_coords

trace_edges = go.Scatter3d(x=x_edges,
                        y=y_edges,
                        z=z_edges,
                        mode='lines',
                        line=dict(color='black', width=2),
                        hoverinfo='none')


#create a trace for the nodes
trace_nodes = go.Scatter3d(x=x_nodes,
                         y=y_nodes,
                        z=z_nodes,
                        mode='markers',
                        marker=dict(symbol='circle',
                                    size=10,
                                    color='blue', #color the nodes according to their community
                                   #colorscale=['green','red'], #either green or mageneta
                                    line=dict(color='blue', width=0.5)),
                        #text=club_labels,
                        #hoverinfo='text'
                        )
axis = dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title='')
layout = go.Layout(title="3D Network",
                width=1000,
                height=1000,
                showlegend=False,
                scene=dict(xaxis=dict(axis),
                        yaxis=dict(axis),
                        zaxis=dict(axis),
                        ),
                margin=dict(t=100),
                hovermode='closest')
data = [trace_edges, trace_nodes]
fig = go.Figure(data=data, layout=layout)

fig.show()
