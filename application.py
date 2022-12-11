from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)
application = app.server
app.layout = html.Div([
	html.H1('Projet Analyse des réseau sociaux: Abdoulaye SARR, Uvs Big data'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                ),style={'margin':19}
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
],style={'padding-left': 60, 'flex': 3})


if __name__ == '__main__':
	#app.run_server(debug=True,port=8080)
    application.run(debug=True, port=8080)