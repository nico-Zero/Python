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
    count_state = 1
    click_count = 0

    def on_button_click(self):
        if self.count_state > 0:
            self.click_count += 1
        else:
            self.click_count -= 1
        print(f"Button clicked for {self.click_count} time")
        self.hello = str(self.click_count)

    def change_state(self, widget):
        print("Button State:- ", widget.state)
        self.count_state *= -1


class MyApp(App):
    pass


MyApp().run()
