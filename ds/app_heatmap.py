import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from credentials import MAPBOX_ACCESS_TOKEN

mapbox_access_token = MAPBOX_ACCESS_TOKEN

df = pd.read_csv('gun-violence-data_01-2013_03-2018_cleaned.csv')

# Feature engineering to combine # of people killed or injured
df['n_killed_injured'] = df['n_killed'] + df['n_injured']
df = df[df['n_killed_injured'] > 3]
df['locations_info'] = df.apply(lambda row: "Location: "+row.city_or_county+\
        "<br>"+"Casualty: "+str(row.n_killed_injured)+\
        "<br>"+"Date: " + str(row.date), axis=1)

site_lat = df.latitude
site_lon = df.longitude
#locations_info = df.city_or_county
locations_info = df.locations_info

data = [
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            color='rgb(165,18,18)',
            opacity=0.5
        ),
        text=locations_info,
        hoverinfo='text'
    ),
    ]
        
layout = go.Layout(
    title='Mass shooting across USA (Jan 2013-March 2018)',
    #autosize=True,
    width=1000,
    height=1000,
    hovermode='closest',
    showlegend=False,
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=2,
        #style='light'
        style='mapbox://styles/shreyasjothish/cjt9fxodx07wf1fm9aj5qljip',
    ),
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=9250)
