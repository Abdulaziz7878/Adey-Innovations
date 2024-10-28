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
                        html.H5("Average Age (°C)", className="card-title"),
                        html.H2(id='average-Age', className="card-text")
                    ])
                ], className="mb-2")
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Average Class (%)", className="card-title"),
                        html.H2(id='average-class', className="card-text")
                    ])
                ], className="mb-2")
            ], md=4),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select Year"),
                    dcc.Dropdown(
                        id='age-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Select class"),
                    dcc.Dropdown(
                        id='class-dropdown',
                        options=[],
                        value=None,
                        clearable=False
                    )
                ])
            ], md=6),
        ], className="mb-4"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='age')
            ], md=6),
            dbc.Col([
                dcc.Graph(id='class')
            ], md=6),
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='fraud-pie')
            ], md=6),
            dbc.Col([
                dcc.Graph(id='age-fraud-distribution')
            ], md=6),
        ]),
    ], fluid=True)
