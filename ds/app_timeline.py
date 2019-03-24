import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('timeline(1).csv')

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
  trace1 = go.Scatter(x = df.date, y = df.incidents,
                      name='Total Incidents', mode = "lines", 
                      marker = dict(color = '#a51212'))
  trace2 = go.Scatter(x = df.date, y = df.n_killed, 
                      name="Total Killed", mode = "lines", 
                      marker = dict(color = '#666666'))
  trace3 = go.Scatter(x = df.date, y = df.n_injured, 
                      name="Total Injured", mode = "lines", 
                      marker = dict(color = '#4f5a62'))

  data = [trace1, trace2, trace3]
  layout = dict(height=350,title = 'Gun Violence Incidents Through the Years',
                legend=dict(orientation="h", x=-.01, y=1), 
                xaxis= dict(title='Time(in Years)', ticklen= 1))
  
  return {'data': data, 'layout': layout}


if __name__ == '__main__':
app.run_server(port=9450)
