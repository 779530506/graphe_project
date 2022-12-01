# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash 
from dash import Dash, html, dcc
from dash import html, dcc, callback, Input, Output,State
from figure import networkGraph,calculdistance
from ville import data
import pandas as pd
#dash.register_page(__name__)

dash.register_page(
    __name__,
    path='/analytics-dashboard',
    title='Our Analytics Dashboard',
    name='Our Analytics Dashboard'
)
villes = []
for ville in data:
    villes.append(ville)
    for v in data[ville]:
        villes.append(v)
villes =list(set(villes))
  

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



layout = html.Div([
    html.Div(children=[
        html.Label('Sélectionner la ville de départ'),
        dcc.Dropdown(villes,"ziginchor",id="input_value1"),

        html.Br(),
        html.Label('Sélectionner la ville d\'arrivée '),
        dcc.Dropdown(villes,'dakar',id="input_value2"),
        html.Br(),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Br(),
        html.Div(id="output_value3"),
        html.Br(),
        html.Div(id="output_value4"),
        html.Br(),
        dcc.Graph(
            id='output_value2'
        ),

        # html.Br(),
        # html.Label('Radio Items'),
        # dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
        
    ], style={'padding': 1, 'flex': 1}),
     


    html.Div(style={'backgroundColor': colors['background']},children=[
   
        dcc.Graph(
            id='output_value1'
        )
    ]),
], )
#style={'display': 'flex', 'flex-direction': 'row'}



@callback(
    Output('output_value1', 'figure'),
    Output('output_value4', component_property='children'),
    Output('output_value2', 'figure'),
    Output('output_value3', component_property='children'),
    
    # Input('input_value1', 'value'),
    # Input('input_value2', 'value'),
    Input('submit-button-state', 'n_clicks'),
    State('input_value1', 'value'),
    State('input_value2', 'value')
    )
def update_figure(n_clicks,ville1,ville2):
    g2,distanceMin = calculdistance(ville1,ville2)
    g1,villeConnecte = networkGraph(ville1,ville2)
    return g1,villeConnecte,g2,distanceMin