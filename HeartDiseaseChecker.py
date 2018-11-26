import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from sklearn.externals import joblib
import numpy as np

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
question_7 = "7. Resting ECG"
question_8 = "8. Max-heart rate achieved"
question_9 = "9. Exercise induced angina"
question_10 = "10. ST depression induced by exercise relative to rest"

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
                    ]),
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
                    ]),
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
                    ]),
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
                    ]),
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
                        dcc.Input(
                            id="heart-rate",
                            value=90
                        )
                    ]),
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
                    ])
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
                        dcc.Input(
                            id="st-depression",
                            value=0
                        )
                    ]),
                    html.Div(children=[
                        html.P(id="st-depression-p")
                    ], className="pt-4")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Result
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Div(children=[
                    html.H5(children='Result:', className="mb-4"),
                    html.P(id="final-output")
                ], className="card-panel")
            ], className="col")
        ], className="row")
    ], className="container py-1"),

    #Submit button
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Button(id='submit-button', children='Go!',
                    className="btn-large waves-effect waves-light")
            ], className="col",
                style={
                    'textAlign': 'center'
            }),
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
    Output(component_id='heart-rate-p', component_property='children'),
    [Input(component_id='heart-rate', component_property='value')]
)

def update_heart_rate(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='induced-angina-p', component_property='children'),
    [Input(component_id='induced-angina', component_property='value')]
)

def update_angina(input_value):
    return 'Your answer is "{}"'.format(input_value)

@app.callback(
    Output(component_id='st-depression-p', component_property='children'),
    [Input(component_id='st-depression', component_property='value')]
)
def update_st_depression(input_value):
    return 'Your answer is "{}"'.format(input_value)

# Callback for submit button
@app.callback(
    Output(component_id='final-output', component_property='children'),
    [Input('submit-button', 'n_clicks')],
    [State('age', 'value'),
     State('gender', 'value'),
     State('chest-pain', 'value'),
     State('blood-pressure', 'value'),
     State('colestrol', 'value'),
     State('blood-sugar', 'value'),
     State('ecg', 'value'),
     State('heart-rate', 'value'),
     State('induced-angina', 'value'),
     State('st-depression', 'value')
    ]
)
def result(n_clicks, age, gender, chest_pain, blood_p, colestrol, blood_s, ecg, heart_rate, induced_a, st_dep):
    # Load the model and return output..
    if(n_clicks > 0):
        instance = np.array([age, gender, chest_pain, blood_p, colestrol, blood_s, ecg, int(heart_rate), induced_a, int(st_dep)])
        reshape = instance.reshape(1, -1)
        result = predict(reshape)
        print(result)

        if(result == [0]):
            return "You don't have a heart disease. Enjoy your day!"
        elif(result == [1]):
            return "you have a heart disease stage 1."
        elif(result == [2]):
            return "you have a heart disease stage 2."
        elif (result == [3]):
            return "you have a heart disease stage 3."
        elif (result == [4]):
            return "you have a heart disease stage 4."
        else:
            print(result);
            return "Error while predicting. Try again."
    else:
        n_clicks+=1


def predict(instance):
    filename_model = "heart_disease_model.mdl"
    model = joblib.load(filename_model)
    return model.predict(instance)

if __name__ == "__main__":
    app.run_server(debug=True)
