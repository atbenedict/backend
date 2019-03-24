import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('gun-violence-data_choropleth.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()}
    )
])


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    scl = [
            [0.0, 'rgb(255,225,225)'],
            [0.2, 'rgb(245,210,203)'],
            [0.4, 'rgb(231,166,153)'],
            [0.6, 'rgb(213,122,105)'],
            [0.8, 'rgb(191,77,60)'],
            [1.0, 'rgb(165,18,18)']
            ]

    df_grouped = filtered_df.groupby('code').sum().reset_index()

    data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = df_grouped['code'],
    z = df_grouped['n_killed_injured'],
    locationmode = 'USA-states',
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "#People Killed or Injured")
    )]


    layout = go.Layout(
    title = go.layout.Title(
        text = str(selected_year) + ' US Gun Violence <br>(Hover for breakdown)'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
    )   

    return {'data': data, 'layout': layout}


if __name__ == '__main__':
    app.run_server(port=9150)
