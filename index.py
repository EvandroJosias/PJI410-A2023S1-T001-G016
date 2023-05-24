from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def Opcao1():
    dados_x = ['2018', '2019', '2020', '2021']
    dados_y = [10, 20, 5, 35]

    fig = px.line(x=dados_x, y=dados_y, title="Vendas x Ano",
                  height=400, width=1000, line_shape='spline')
    return html.Div(children=[
        html.H1(children='Videogame Sales Project', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            Gráfico de vendas globais por jogo e plataforma este grafico foi gerado pensando em fazer uma analise XPTO mostrando que nós conseguimos fazer a analise de dados conforme solicitado
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'align': 'center'}
        ),
        html.H1('_', style={'fontSize': 30, 'margin': '20px'})
    ])


def Opcao2():
    df = pd.read_csv('dataset.csv', encoding="utf-8")
    fig = px.scatter(df, x="User_Score", y="Critic_Score", color="Platform")
    return html.Div(children=[
        html.H1(children='Videogame Sales Project'),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            Gráfico de pontuação do usuário e crítica por plataforma
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])


def Opcao3():
    df = pd.read_csv('dataset.csv', encoding="utf-8")
    fig = px.scatter(df, x="User_Score", y="Critic_Score", color="Platform")
    return html.Div(children=[
        html.H1(children='Videogame Sales Project'),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            Gráfico de pontuação do usuário e crítica por plataforma
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])


app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'margin': '20px', 'padding': '20px 20px 20px 20px'},
                      children=[
    html.H1('Projeto Integrador em Computação IV - Turma 001 - Grupo 016',
            style={'color': colors['text'], 'fontSize': 40, 'textAlign': 'center', 'margin': '20px'}),
    html.H3('Escolha o Grafico : ', style={
            'color': colors['text'], 'fontSize': 25, 'textAlign': 'left', 'margin':'20px'}),
    dcc.Dropdown(['Vendas', 'Ranking', 'Produtor'], 'Vendas', id='mydropdown'),
    html.Div(id='dd-output-container')
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('mydropdown', 'value')
)
def update_output(value):
    if value == 'Vendas':
        return Opcao1()
    elif value == 'Ranking':
        return Opcao2()
    else:
        return Opcao3()


if __name__ == '__main__':
    app.run_server(debug=True)
