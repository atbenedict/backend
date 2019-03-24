import dash
from jobs import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from jobs.routes import *
from import plotly.graph_objs as go
import folium
import dash_table_experiments as dt

app.layout = html.Div([
    html.H1('Gun Violence Across The US')
    html.Iframe(srcDoc = open('Folium Map(edited).html', 'r').read(),
                width = '100%', height ='600')
    ]
)
