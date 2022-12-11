
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import networkx as nx
from ville import data
from sqlalchemy import create_engine # database connection
def networkGraph(source,destination):
  
    edges = []
    for e in data:
        for v in data[e]:
            edges.append([e,v,{"weight":data[e][v] }]) 
    G = nx.Graph()
    G.add_nodes_from(data)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)

    #G = calculdistance(source,destination)
    # edges trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color='black', width=1),
        hoverinfo='none',
        showlegend=False,
        mode='lines')

    # nodes trace
    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=text,
        mode='markers+text',
        showlegend=False,
        hoverinfo='none',
        marker=dict(
            color='pink',
            size=35,
            line=dict(color='red', width=1)))

    # layout
    layout = dict(plot_bgcolor='white',
                  paper_bgcolor='white',
                  margin=dict(t=10, b=10, l=10, r=10, pad=0),
                  xaxis=dict(linecolor='yellow',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True),
                  yaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True))

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)

    #pageranks = nx.pagerank(G) 
    villeConnecte = sorted(G.degree, key=lambda x: x[1], reverse=True)
    print(villeConnecte[0][1])
    message = "la ville la plus connectée est  {} avec {}  liaisons.".format(villeConnecte[0][0],villeConnecte[0][1])
    message += "  Et la ville la moins connectée est  {} avec {} liaisons".format(villeConnecte[-1][0],villeConnecte[-1][1])

    return fig , message

def calculdistance(source,destination):
    if not source:
        source = "dakar"
        destination = "Ziguinchor"
    G = getGraphe()

    plt = nx.shortest_path(G, source=source, target=destination, weight="weight")
    distanceMin = nx.shortest_path_length(G, source=source, target=destination, weight="weight")
    edges=[]
    G = nx.Graph()
    for i,ville in enumerate(plt):
        if i!=0:
            G.add_node(ville)
            edges.append((plt[i-1],ville))
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)

    edge_x = []
    edge_y = []

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color='black', width=1),
        hoverinfo='none',
        showlegend=False,
        mode='lines')

    # nodes trace
    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=text,
        mode='markers+text',
        showlegend=False,
        hoverinfo='none',
        marker=dict(
            color='pink',
            size=50,
            line=dict(color='black', width=1)))

    # layout
    layout = dict(plot_bgcolor='#357A90',
                  paper_bgcolor='white',
                  margin=dict(t=10, b=10, l=10, r=10, pad=0),
                  xaxis=dict(
                    # linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True),
                  yaxis=dict(
                    # linecolor='red',
                             showgrid=False,
                             showticklabels=False,
                            #  mirror=True
                             )
                 )

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
    message = "la distance minimum  entre {} et {} est de {} ".format(source,destination,distanceMin)

    return fig,message
    
def getGraphe():
    edges = []
    for e in data:
        for v in data[e]:
            edges.append([e,v,{"weight":data[e][v] }]) 
    G = nx.Graph()
    G.add_nodes_from(data)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)

    return G

def getCarte():
    edges = []
    for e in data:
        for v in data[e]:
            edges.append([e,v,{"weight":data[e][v] }]) 
    G = nx.Graph()
    G.add_nodes_from(data)
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)

    #G = calculdistance(source,destination)
    # edges trace
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(color='black', width=1),
        hoverinfo='none',
        showlegend=False,
        mode='lines')

    # nodes trace
    node_x = []
    node_y = []
    text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(node)

    node_trace = go.Scatter(
        x=node_x, y=node_y, text=text,
        mode='markers+text',
        showlegend=False,
        hoverinfo='none',
        marker=dict(
            color='yellow',
            size=30,
            line=dict(color='green', width=1)))

    # layout
    layout = dict(plot_bgcolor='#357A90',
                  paper_bgcolor='white',
                  margin=dict(t=10, b=10, l=10, r=10, pad=0),
                  xaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True),
                  yaxis=dict(linecolor='black',
                             showgrid=False,
                             showticklabels=False,
                             mirror=True))

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)

    return fig