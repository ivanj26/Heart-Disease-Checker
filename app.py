import dash
from dash.dependencies import Input, Output, State
import flask, os
from sklearn.externals import joblib
import numpy as np

from view import View

app = dash.Dash(__name__, external_stylesheets=['http://localhost:8050/css/app.css'])
View.render_view(app)


@app.callback(
    Output(component_id='age-out', component_property='children'),
    [Input(component_id='age', component_property='value')]
)
def update_age(age):
    return 'Your answer is {}'.format(age)


@app.callback(
    Output(component_id='result', component_property='children'),
    [Input('submit', 'n_clicks')],
    [State('age', 'value'),
     State('gender', 'value'),
     State('chest-pain-type', 'value'),
     State('blood-pressure', 'value'),
     State('cholesterol', 'value'),
     State('blood-sugar', 'value'),
     State('ecg', 'value'),
     State('heart-rate', 'value'),
     State('exercise-induced-angina', 'value'),
     State('st-depression', 'value')]
)
def result(n_clicks, age, gender, chest_pain, blood_p, colestrol, blood_s, ecg, heart_rate, induced_a, st_dep):
    if n_clicks > 0:
        instance = np.array(
            [age, gender, chest_pain, blood_p, colestrol, blood_s, ecg, int(heart_rate), induced_a, int(st_dep)])
        reshape = instance.reshape(1, -1)
        prediction_value = predict(reshape)
        print(prediction_value)
        return prediction_value
    else:
        n_clicks += 1
    # Load the model and return output..


def predict(instance):
    filename_model = "heart_disease_model.mdl"
    model = joblib.load(filename_model)
    return model.predict(instance)


css_directory = '{0}/css/'.format(os.getcwd())


@app.server.route('/css/<stylesheet>')
def serve_css(stylesheet):
    print(stylesheet)
    print(css_directory)
    return flask.send_from_directory(css_directory, stylesheet)


if __name__ == '__main__':
    app.run_server(debug=True)
