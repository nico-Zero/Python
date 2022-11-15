from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty


class WidgetsExample(GridLayout):
    hello = StringProperty("Hello!")
    state = BooleanProperty(True)
    click_count = 0
    number_x = 1

    def on_button_click(self):
        self.click_count += self.number_x
        print(f"Button clicked for {self.click_count} time")
        self.hello = str(self.click_count)

    def change_state(self, widget):
        print("Button State:- ", widget.state)
        if self.state:
            self.state = False
            widget.text = "ON"
        else:
            self.state = True
            widget.text = "OFF"

    def change_way(self):
        self.number_x *= -1


class MyApp(App):
    pass


MyApp().run()
