import dash
from dash import html, dcc, callback, Input, Output,State
from figure import getCarte
dash.register_page(__name__, path='/',name="Carte du Sénégal en mode graphe")

layout = html.Div([
    html.Div(children=[
   
        dcc.Graph(
            id='output_value1',
            figure=getCarte()
        )
    ]),
        
    ], style={'padding': 1, 'flex': 1}),
     


    
#style={'display': 'flex', 'flex-direction': 'row'}



# @callback(
#     Output('output_value1', 'figure'),
#     )
# def update_figure():
#     return getCarte()