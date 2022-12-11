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
    title='Chemin le plus court entre deux ville ',
    name='Chemin le plus court'
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
        html.Label('Sélectionner la ville de départ',style={'color': 'green', 'font-size': '1.2rem'}),
        dcc.Dropdown(villes,"ziginchor",id="input_value1",style={'color': 'green', 'font-size': '1.2rem'}),

        html.Br(),
        html.Label('Sélectionner la ville d\'arrivée ',style={'color': 'blue', 'font-size': '1.2rem'}),
        dcc.Dropdown(villes,'dakar',id="input_value2",style={'color': 'blue', 'font-size': '1.2rem'}),
        html.Br(),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit',
        style={'margin': 1,'background':"blue",'height':"2rem",'width':"100%","color":"white",
        "font-size":"1.5rem", "font-weight": "bold"}),
        html.Br(),
        html.Br(),
        html.Div(id="output_value3",style={'padding': 4,'color':"red", "font-size":"1.5rem", "font-weight": "bold"}),
        html.Br(),
        html.Div(id="output_value4",style={'padding': 4,'color':"blue", "font-size":"1.5rem", "font-weight": "bold"}),
        html.Br(),
        dcc.Graph(
            id='output_value2'
        ),

        # html.Br(),
        # html.Label('Radio Items'),
        # dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
        
    ], style={'padding-left': 20,'padding-top': 2,'padding-right': 70,'padding-bottom': 1, 'flex': 1}),
     


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