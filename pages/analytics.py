# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash 
from dash import Dash, html, dcc
from dash import html, dcc, callback, Input, Output,State
from figure import networkGraph,calculdistance
from ville import data

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

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



layout = html.Div([
    html.Div(children=[
        html.Label('Sélectionner la ville de départ'),
        dcc.Dropdown(villes,"Ziguinchor",id="input_value1"),

        html.Br(),
        html.Label('Sélectionner la ville d\'arrivée '),
        dcc.Dropdown(villes,'dakar',id="input_value2"),
        html.Br(),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Br(),
        dcc.Graph(
            id='output_value2'
        ),

        # html.Br(),
        # html.Label('Radio Items'),
        # dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
        
    ], style={'padding': 10, 'flex': 1}),
     

    # html.Div(children=[
    #     html.Label('Checkboxes'),
    #     dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
    #                   ['Montréal', 'San Francisco']
    #     ),

    #     html.Br(),
    #     html.Label('Text Input'),
    #     dcc.Input(value='MTL', type='text'),

    #     html.Br(),
    #     html.Label('Slider'),
    #     dcc.Slider(
    #         min=0,
    #         max=9,
    #         marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
    #         value=5,
    #     ),
    # ], style={'padding': 10, 'flex': 1}),

    html.Div(style={'backgroundColor': colors['background']},children=[
   
        dcc.Graph(
            id='output_value1'
        )
    ]),
], )
#style={'display': 'flex', 'flex-direction': 'row'}



@callback(
    Output('output_value1', 'figure'),
    Output('output_value2', 'figure'),
    # Input('input_value1', 'value'),
    # Input('input_value2', 'value'),
    Input('submit-button-state', 'n_clicks'),
    State('input_value1', 'value'),
    State('input_value2', 'value')
    )
def update_figure(n_clicks,ville1,ville2):
    return networkGraph(ville1,ville2),calculdistance(ville1,ville2)