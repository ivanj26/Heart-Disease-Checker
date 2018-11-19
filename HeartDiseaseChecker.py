import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#Add styles
external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css', 'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css']

#Variables
app_title = "Heart Disease Checker"
authors = "Authors:\nJonathan Tjandra - 13516058\nIvan Jonathan - 13516059\nI Putu Eka Surya - 13516061\nShandy - 13516097\nPutu Gery Wahyu - 13516100"
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

question_1 = "1. How old are you?"
question_2 = "2. What is your gender?"
question_3 = "3. What is your chest pain type?"
question_4 = "4. How's your blood pressure? (in mmHg)"
question_5 = "5. How's your colestrol? (in mg/dl)"
question_6 = "6. Do you suffer blood sugar?"
question_7 = "7. ..."
question_8 = "8. ..."
question_9 = "9. ..."
question_10 = "10. ..."
question_11 = "11. ..."
question_12 = "12. ..."
question_13 = "13. ..."

#app root
app.layout = html.Div(children=[
    # Header card
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H4(children=app_title,
                    style={
                        'textAlign': 'center'
                    }),
                    html.Div(children=[
                        html.Pre(children=authors,
                        style={
                            'textAlign': 'center',
                            'fontSize': '12'
                        })
                    ])
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 1
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_1, className="mb-4"),
                    html.Div(children=[
                        dcc.Slider(
                            id="age",
                            min=1,
                            max=100,
                            marks={i: str(i) if i % 10 == 0 else "" for i in range(1,100)},
                            value=50
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="age-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 2
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_2, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="gender",
                            options=[
                                {'label': 'Male', 'value': 1},
                                {'label': 'Female', 'value': 0}
                            ],
                            value=1
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P()
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 3
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_3, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="chest-pain",
                            options=[
                                {'label': 'Typical Angina', 'value': 1},
                                {'label': 'Atypical Angina', 'value': 2},
                                {'label': 'Non-anginal', 'value': 3},
                                {'label': 'Asymptotic', 'value': 4},
                            ],
                            value=1
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P()
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),
])

#Callback
@app.callback(
    Output(component_id='age-p', component_property='children'),
    [Input(component_id='age', component_property='value')]
)

def update_output_div(input_value):
    return 'Your answer is "{}"'.format(input_value)


if __name__ == "__main__":
    app.run_server(debug=True)
