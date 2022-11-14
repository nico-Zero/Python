from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class WidgetsExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_button_click(self, number):
        print("Button clicked", number)


class MyApp(App):
    pass


MyApp().run()
