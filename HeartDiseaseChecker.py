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
                        html.P(id="gender-p")
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
                        html.P(id="chest-pain-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 4
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_4, className="mb-4"),
                    html.Div(children=[
                        dcc.Slider(
                            id="blood-pressure",
                            min=70,
                            max=190,
                            marks={i: str(i) if i % 10 == 0 else "" for i in range(70,190)},
                            value=100
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="blood-pressure-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 5
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_5, className="mb-4"),
                    html.Div(children=[
                        dcc.Slider(
                            id="colestrol",
                            min=140,
                            max=300,
                            marks={i: str(i) if i % 10 == 0 else "" for i in range(140,300)},
                            value=180
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="colestrol-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 6
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_6, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="blood-sugar",
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0}
                            ],
                            value=0
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="blood-sugar-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 7
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_7, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="ecg",
                            options=[
                                {'label': 'Normal', 'value': 0},
                                {'label': 'Having ST-T wave abnormality', 'value': 1},
                                {'label': 'Left ventricular hyperthrophy', 'value': 2}
                            ],
                            value=0
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="ecg-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 8
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_8, className="mb-4"),
                    html.Div(children=[
                        # dcc.Dropdown(
                        #     id="heart-rate",
                        #     options=[
                        #         {'label': 'Yes', 'value': 1},
                        #         {'label': 'No', 'value': 0}
                        #     ],
                        #     value=0
                        # )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="heart-rate-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 9
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_9, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="induced-angina",
                            options=[
                                {'label': 'Yes', 'value': 1},
                                {'label': 'No', 'value': 0}
                            ],
                            value=0
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="induced-angina-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 10
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_10, className="mb-4"),
                    html.Div(children=[
                        # dcc.Dropdown(
                        #     id="st-depression",
                        #     options=[
                        #         {'label': 'Yes', 'value': 1},
                        #         {'label': 'No', 'value': 0}
                        #     ],
                        #     value=0
                        # )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="st-depression-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 11
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_11, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="st-segment",
                            options=[
                                {'label': 'Upsloping', 'value': 1},
                                {'label': 'Flat', 'value': 2},
                                {'label': 'Downsloping', 'value': 3}
                            ],
                            value=2
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="st-segment-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 12
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_12, className="mb-4"),
                    html.Div(children=[
                        # dcc.Dropdown(
                        #     id="vessel",
                        #     options=[
                        #         {'label': 'Upsloping', 'value': 1},
                        #         {'label': 'Flat', 'value': 2},
                        #         {'label': 'Downsloping', 'value': 3}
                        #     ],
                        #     value=0
                        # )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="vessel-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Question 13
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children=question_13, className="mb-4"),
                    html.Div(children=[
                        dcc.Dropdown(
                            id="thal",
                            options=[
                                {'label': 'Normal', 'value': 3},
                                {'label': 'Fixed defect', 'value': 6},
                                {'label': 'Reversable defect', 'value': 7}
                            ],
                            value=3
                        )
                    ], className="mb-4"),
                    html.Div(children=[
                        html.P(id="thal-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),
])

#Callbacks
@app.callback(
    Output(component_id='age-p', component_property='children'),
    [Input(component_id='age', component_property='value')]
)

def update_age(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='gender-p', component_property='children'),
    [Input(component_id='gender', component_property='value')]
)

def update_gender(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='chest-pain-p', component_property='children'),
    [Input(component_id='chest-pain', component_property='value')]
)

def update_chest_pain(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='blood-pressure-p', component_property='children'),
    [Input(component_id='blood-pressure', component_property='value')]
)

def update_blood_pressure(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='colestrol-p', component_property='children'),
    [Input(component_id='colestrol', component_property='value')]
)

def update_colestrol(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='blood-sugar-p', component_property='children'),
    [Input(component_id='blood-sugar', component_property='value')]
)

def update_blood_sugar(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='ecg-p', component_property='children'),
    [Input(component_id='ecg', component_property='value')]
)

def update_ecg(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='induced-angina-p', component_property='children'),
    [Input(component_id='induced-angina', component_property='value')]
)

def update_angina(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='st-segment-p', component_property='children'),
    [Input(component_id='st-segment', component_property='value')]
)

def update_segment(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='thal-p', component_property='children'),
    [Input(component_id='thal', component_property='value')]
)

def update_thal(input_value):
    return 'Your answer is "{}"'.format(input_value)

if __name__ == "__main__":
    app.run_server(debug=True)
