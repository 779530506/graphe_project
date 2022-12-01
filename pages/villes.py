# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd
import dash

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df = pd.read_json("/home/abdoulayesarr/Documents/MasterBigdata/analyse_reseaux_sociaux/avocado_analytics/villes.json")
ville =set().union(df.columns,df.index)

def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in ["ville"]])
        ),
        html.Tbody([
            html.Tr([
                html.Td(v) for v in ville
            ]) for i in range(min(len(ville), max_rows))
        ])
    ])



layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])


