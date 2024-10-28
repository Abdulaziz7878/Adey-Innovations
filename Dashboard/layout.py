from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(app):
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Fraud detection Dashboard"), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H2(children='Interactive visualization of fraud detection data'), className="mb-4")
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Average Temperature (°C)", className="card-title"),
                        html.H2(id='average-temperature', className="card-text")
                    ])
                ], className="mb-2")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Average Humidity (%)", className="card-title"),
                        html.H2(id='average-humidity', className="card-text")
                    ])
                ], className="mb-2")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Average Wind Speed (km/h)", className="card-title"),
                        html.H2(id='average-windspeed', className="card-text")
                    ])
                ], className="mb-2")
            ], md=4),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select Year"),
                    dcc.Dropdown(
                        id='year-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select Month"),
                    dcc.Dropdown(
                        id='month-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='temperature-over-time')
            ], md=6),
            dbc.Col([
                dcc.Graph(id='humidity-over-time')
            ], md=6),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='weather-condition-pie')
            ], md=6),
            dbc.Col([
                dcc.Graph(id='windspeed-distribution')
            ], md=6),
        ]),
    ], fluid=True)
