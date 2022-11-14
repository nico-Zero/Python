from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    hello = StringProperty("Hello!")
    click_count = 0

    def on_button_click(self):
        self.click_count += 1
        print(f"Button clicked for {self.click_count} time")
        self.hello = f"Clicked {self.click_count}"


class MyApp(App):
    pass


MyApp().run()
