import dash
from dash.dependencies import Input, Output, State
import flask, os
from sklearn.externals import joblib
import numpy as np
import dash_html_components as html
import dash_core_components as core
import plotly.graph_objs as go


from view import View

app = dash.Dash(__name__, external_stylesheets=['http://localhost:8050/css/app.css'])
View.render_view(app)


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
            [int(age), int(gender), int(chest_pain), int(blood_p), int(colestrol), int(blood_s), int(ecg), int(heart_rate), int(induced_a), int(st_dep)])
        reshape = instance.reshape(1, -1)
        print(reshape)
        predict_result = predict(reshape)
        print(predict_result)

        if predict_result == [0]:
            message = "You don't have a heart disease. Enjoy your day!"
        elif predict_result == [1]:
            message = "You have a heart disease stage 1."
        elif predict_result == [2]:
            message = "You have a heart disease stage 2."
        elif predict_result == [3]:
            message = "You have a heart disease stage 3."
        elif predict_result == [4]:
            message = "you have a heart disease stage 4."
        else:
            print(predict_result)
            return "Error while predicting. Try again."

        return [html.H2(children=message, className='result-text'), core.Graph(
            figure=go.Figure(
                data=[
                    go.Pie(
                        values=predict_proba(reshape)[0],
                        labels=['Stage 0', 'Stage 1', 'Stage 2', 'Stage 3', 'Stage 4']
                    )
                ],
                layout=go.Layout(
                    title='Heart disease stage probability',
                    showlegend=True
                )
            )
        )]
    else:
        n_clicks += 1
    # Load the model and return output..


def predict(instance):
    filename_model = "heart_disease_model.mdl"
    model = joblib.load(filename_model)
    return model.predict(instance)


def predict_proba(instance):
    filename_model = "heart_disease_model.mdl"
    model = joblib.load(filename_model)
    print(model.predict_proba(instance))
    return model.predict_proba(instance)


css_directory = '{0}/css/'.format(os.getcwd())


@app.server.route('/css/<stylesheet>')
def serve_css(stylesheet):
    print(stylesheet)
    print(css_directory)
    return flask.send_from_directory(css_directory, stylesheet)


res_directory = '{0}/res/'.format(os.getcwd())


@app.server.route('/res/<resource>')
def serve_res(resource):
    return flask.send_from_directory(res_directory, resource)


if __name__ == '__main__':
    app.run_server(debug=True)
