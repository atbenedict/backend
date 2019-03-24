import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df_load = pd.read_csv('gun-violence-data_01-2013_03-2018_cleaned.csv')

# Considering only top 10 states with most gun violence per 10,000 ppl
df = df_load[(df_load.state == 'Alaska') |
             (df_load.state == 'Delaware') |
             (df_load.state == 'Louisiana') |
             (df_load.state == 'South Carolina') |
             (df_load.state == 'Illinois') |
             (df_load.state == 'Mississippi') |
             (df_load.state == 'Tennessee') |
             (df_load.state == 'Alabama') |
             (df_load.state == 'Missouri') |
             (df_load.state == 'Maryland')].copy()

# Feature engineering to combine # of people killed or injured
df['n_killed_injured'] = df['n_killed'] + df['n_injured']
df = df[df['n_killed_injured'] > 3]

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
    traces = []
    for i in filtered_df.state.unique():
        df_by_state = filtered_df[filtered_df['state'] == i]
        traces.append(go.Scatter(
            x=df_by_state['date'],
            y=df_by_state['n_killed_injured'],
            text=df_by_state['city_or_county'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Date'},
            # Considering only Mass shooting scenario
            yaxis={'title': 'At least 4 People Killed or Injured', 'range': [0, 20]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(port=9050)
