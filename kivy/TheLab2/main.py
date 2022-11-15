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
    number_x = 1
    click_count = 0
    button_state = BooleanProperty(False)
    slider_state = BooleanProperty(False)
    display = StringProperty(str(click_count))

    def on_button_click(self):
        self.click_count += self.number_x
        print(f"Button clicked for {self.click_count} time")
        self.display = str(self.click_count)

    def change_state(self, widget):
        print("Button state:- ", widget.state)
        if self.button_state:
            self.button_state = False
            widget.text = "OFF"
        else:
            self.button_state = True
            widget.text = "ON"

    def change_way(self, widget):
        print("Switch:- ", widget.active)
        self.number_x *= -1
        self.slider_state = widget.active

    def update_value(self, widget):
        self.display = str(round(widget.value))
        self.click_count = round(widget.value)


class MyApp(App):
    pass


MyApp().run()
