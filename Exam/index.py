from dash import html
from dash.dependencies import Input, Output
from dash import dcc
from app import app
from dashboard_a import layout as layout_a
from dashboard_b import layout as layout_b

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Дашборд А', href='/dashboard-a', className='dashboard-link'),
        dcc.Link('Дашборд Б', href='/dashboard-b', className='dashboard-link'),
    ], className='link-container'),
    html.Div(id='page-content')
], className='main-container')


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard-a':
        return layout_a
    elif pathname == '/dashboard-b':
        return layout_b
    else:
        return 'Выберите дашборд'


if __name__ == '__main__':
    app.run_server(debug=True)
