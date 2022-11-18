from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GalaxyApp(App):
    pass


GalaxyApp().run()
