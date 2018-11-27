import dash_html_components as html
import dash_core_components as core
from component.Header import Header


class View:
    gender_options = [
        {'label': 'Male', 'value': 1},
        {'label': 'Female', 'value': 0}
    ]

    chest_pain_type_options = [
        {'label': 'Typical Angina', 'value': 1},
        {'label': 'Atypical Angina', 'value': 2},
        {'label': 'Non-anginal', 'value': 3},
        {'label': 'Asymptotic', 'value': 4}
    ]

    yes_no_options = [
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0}
    ]

    ecg_options = [
        {'label': 'Normal', 'value': 0},
        {'label': 'Having ST-T wave abnormality', 'value': 1},
        {'label': 'Left ventricular hypertrophy', 'value': 2}
    ]

    peak_st_segment_options = [
        {'label': 'Upsloping', 'value': 1},
        {'label': 'Flat', 'value': 2},
        {'label': 'Downsloping', 'value': 3}
    ]

    amount_major_vessels_options = [
        {'label': '1', 'value': 1},
        {'label': '2', 'value': 2},
        {'label': '3', 'value': 3}
    ]

    thal_status_options = [
        {'label': 'Normal', 'value': 3},
        {'label': 'Fixed defect', 'value': 6},
        {'label': 'Reversable defect', 'value': 7}
    ]

    @staticmethod
    def render_view(app):
        app.layout = html.Div(children=[
            html.Div(children=[
                Header().view(),
                html.Div(children=[
                    html.H2(children='How old are you?'),
                    core.Input(
                        id='age',
                        className='textbox',
                        value=16
                    ),
                    html.P(id='age-out')
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='What is your gender?'),
                    core.Dropdown(
                        id='gender',
                        options=View.gender_options,
                        value=1
                    )
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='What type of chest pain did you feel?'),
                    core.Dropdown(
                        id='chest-pain-type',
                        options=View.chest_pain_type_options,
                        value=1
                    )
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='How is your blood pressure?'),
                    core.Slider(
                        id='blood-pressure',
                        min=70,
                        max=190,
                        step=None,
                        marks={i: str(i) for i in range(70, 200, 10)},
                        value=100
                    )
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='How is your cholesterol'),
                    core.Input(
                        id='cholesterol',
                        className='textbox',
                        value=150
                    )
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='Do you have high blood sugar level?'),
                    core.Dropdown(
                        id='blood-sugar',
                        options=View.yes_no_options,
                        value=0
                    )
                ], className='card question'),
                html.Div(children=[
                    html.H2(children='What is your resting ECG?'),
                    core.Dropdown(
                        id='ecg',
                        options=View.ecg_options,
                        value=0
                    )
                ]),
                html.Div(children=[
                    html.H2(children='What is your maximum heart beat rate?'),
                    core.Input(
                        id='heart-rate',
                        className='textbox',
                        value=90
                    )
                ]),
                html.Div(children=[
                    html.H2(children='Do you have exercise-induced angina?'),
                    core.Dropdown(
                        id='exercise-induced-angina',
                        options=View.yes_no_options,
                        value=0
                    )
                ]),
                html.Div(children=[
                    html.H2(children='Number of ST depression induced by exercise relative to rest?'),
                    core.Input(
                        id='st-depression',
                        className='textbox',
                        value=0
                    )
                ]),
                html.Div(children=[
                    html.H2(children='What is your peak exercise ST segment?'),
                    core.Dropdown(
                        id='peak-st-segment',
                        options=View.peak_st_segment_options,
                        value=1
                    )
                ]),
                html.Div(children=[
                    html.H2(children='How many major vessels colored by flourosopy?'),
                    core.Dropdown(
                        id='amount-major-vessels',
                        options=View.amount_major_vessels_options,
                        value=1
                    )
                ]),
                html.Div(children=[
                    html.H2(children='What is your thal status?'),
                    core.Dropdown(
                        id='thal-status',
                        options=View.thal_status_options,
                        value=3
                    )
                ]),
                html.Button(id='submit', children='Calculate result'),
                html.Div(children=[
                    html.H2(id='result')
                ])
            ], className='container')
        ], className='root')