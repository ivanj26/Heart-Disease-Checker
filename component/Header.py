import dash_html_components as html


class Header:

    def __init__(self) -> None:
        self.app_title = 'Heart Disease Checker'

    def view(self):
        return html.Div(children=[
            html.H1(children=self.app_title)
        ], className='box')
