import dash_html_components as html


class Header:

    def __init__(self) -> None:
        self.app_title = 'Heart Disease Checker'

    def view(self):
        return html.Div(children=[
            html.Div(children=[
                html.Img(src='http://localhost:8050/res/red-cross.png', className='header-image'),
                html.H1(children=self.app_title, className='header-title')
            ], className='header'),
            html.P(children='Fill out all the form to know how susceptible you are to heart disease')
        ], className='box')
