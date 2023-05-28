from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np 

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Define função que agrupa score
def score_group(score):
    print(score)
    if score == '':
        vmValue = 0
    else:
        vmValue = float(score)
    if vmValue >= 90:
        return '90-100'
    elif vmValue >= 80:
        return '80-89'
    elif vmValue >= 70:
        return '70-79'
    elif vmValue >= 60:
        return '60-69'
    elif vmValue >= 50:
        return '50-59'
    else:
        return '0-49'
    

def Stand():

    return html.Div(children=[
        html.H1(children='Informações Gerais', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),
        html.Br(),
        # Cria Div com um gráfico de barras
        html.Div(children='''
            Esta aplicação foi desenvolvida com o objetivo de apresentar Gráficos provenientes da Analise de Dados do dataset de Games obtido no Kaggle.
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        html.Br(),
        html.Div(children='''
            Escolha o grafico na opção acima e será apresento uma pequena Analise textual e o Grafico que demostrara o resultado obtido.
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H1('_', style={'fontSize': 30, 'margin': '20px'})
    ])

def Opcao1():
    #Carrega o Dataset
    df = pd.read_csv('dataset.csv', encoding="utf-8")

    df["User_Score"] = df["User_Score"].replace("tbd", np.nan).astype(float)
    
    #Agrupa Score
    df['Score_Group1'] = (df['User_Score']*10).apply(lambda x: score_group(x))

    top = df[['Name', 'Genre']].groupby(['Genre']).count().sort_values('Name', ascending=False).reset_index()[:15]
    pack = []
    for x in top['Genre']:
        pack.append(x)

    df_platform = df[['Genre', 'Score_Group1', 'Global_Sales']].groupby(
        ['Genre','Score_Group1']).median().reset_index().pivot( index='Genre', columns='Score_Group1', values='Global_Sales')
    
    fig = px.imshow(df_platform)
    #plt.ylabel('', fontsize=14) 
    #plt.xlabel('Score group \n', fontsize=12)
    return html.Div(children=[
        html.H1(children='Genero vs Usuário Score', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            A comparação dos mapas de calor da avaliação dos críticos em função da venda global mostrou bem menos correlações do que o mapa de calor com a avaliação dos usuários, o que sugere que seja melhor usar o User_Score, pois contem mais informação.
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
    #Carrega o Dataset
    df = pd.read_csv('dataset.csv', encoding="utf-8")

    df["User_Score"] = df["User_Score"].replace("tbd", np.nan).astype(float)
    
    #Agrupa Score
    df['Score_Group'] = df['Critic_Score'].apply(lambda x: score_group(x))

    top = df[['Name', 'Genre']].groupby(['Genre']).count().sort_values('Name', ascending=False).reset_index()[:15]
    pack = []
    for x in top['Genre']:
        pack.append(x)

    df_platform = df[['Genre', 'Score_Group', 'Global_Sales']].groupby(
        ['Genre','Score_Group']).median().reset_index().pivot( index='Genre', columns='Score_Group', values='Global_Sales')
    
    fig = px.imshow(df_platform)
    #plt.ylabel('', fontsize=14) 
    #plt.xlabel('Score group \n', fontsize=12)
    return html.Div(children=[
        html.H1(children='Genero vs Crítica Score', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            A comparação dos mapas de calor da avaliação dos críticos em função da venda global mostrou bem menos correlações do que o mapa de calor com a avaliação dos usuários, o que sugere que seja melhor usar o User_Score, pois contem mais informação.
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'align': 'center'}
        ),
        html.H1('_', style={'fontSize': 30, 'margin': '20px'})
    ])


def Opcao3():
    #Carrega o Dataset
    df = pd.read_csv('dataset.csv', encoding="utf-8")

    df["User_Score"] = df["User_Score"].replace("tbd", np.nan).astype(float)
    
    fig = px.histogram( df, x="User_Score", y="Critic_Score", marginal="box", hover_data=df.columns )

    return html.Div(children=[
        html.H1(children='Mapa Score (Usuário vs Crítica)', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            Com isso vimos uma boa correlação linear entre User_Score e Critic_Score, principalmente para notas mais altas, o que sugere que devamos usar ou outra variável para predições.
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'align': 'center'}
        ),
        html.H1('_', style={'fontSize': 30, 'margin': '20px'})
    ])

# Função que cria o quarto gráfico
def Opcao4():
    df = pd.read_csv('dataset.csv', encoding="utf-8")

    df["User_Score"] = df["User_Score"].replace("tbd", np.nan).astype(float)

    df['Score_Group1'] = (df['User_Score']*10).apply(lambda x: score_group(x))

    col = ['Genre','Global_Sales','Score_Group1']
    df  = df[col].dropna()

    fig = px.scatter(df, x="Global_Sales", y="Score_Group1")
    return html.Div(children=[
        html.H1(children='Aplicação Algorítmos de Agrupamentos (Clusterização)', style={
                'color': colors['text'], 'fontSize': 30, 'textAlign': 'center'}),

        # Cria Div com um gráfico de barras
        html.Div(children='''
            
        ''', style={
            'color': colors['text'], 'fontSize': 25, 'margin':'20px', 'textAlign': 'justify'}),
        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'align': 'center'}
        ),
        html.H1('_', style={'fontSize': 30, 'margin': '20px'})
    ])


app = Dash(__name__)

server = app.server

app.layout = html.Div(style={'backgroundColor': colors['background'], 'margin': '20px', 'padding': '20px 20px 20px 20px'},
                      children=[
    html.H1('Projeto Integrador em Computação IV - Turma 001 - Grupo 016',
            style={'color': colors['text'], 'fontSize': 40, 'textAlign': 'center', 'margin': '20px'}),
    html.H3('Escolha o Grafico : ', style={
            'color': colors['text'], 'fontSize': 25, 'textAlign': 'left', 'margin':'20px'}),
    dcc.Dropdown(['Genero vs Usuário Score', 'Genero vs Crítica Score', 'Mapa Score (Usuário vs Crítica)','Aplicação Algorítmos de Agrupamentos (Clusterização)'], '', id='mydropdown'),
    html.Div(id='dd-output-container')
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('mydropdown', 'value')
)
def update_output(value):
    if value == 'Genero vs Usuário Score':
        return Opcao1()
    elif value == 'Genero vs Crítica Score':
        return Opcao2()
    if value == 'Mapa Score (Usuário vs Crítica)':
        return Opcao3()
    if value == 'Aplicação Algorítmos de Agrupamentos (Clusterização)':
        return Opcao4()
    else:
        return Stand()


if __name__ == '__main__':
    app.run_server(debug=True)
