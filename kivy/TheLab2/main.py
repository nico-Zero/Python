from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty


class WidgetsExample(GridLayout):
    number_x = 1
    click_count = 0
    display = StringProperty(str(click_count))
    text_input = StringProperty()

    def on_button_click(self):
        self.click_count += self.number_x
        print(f"Button clicked for {self.click_count} time")
        self.display = str(self.click_count)

    def change_state(self, widget):
        print("Button state:- ", widget.state)
        if widget.state == "down":
            widget.text = "ON"
        else:
            widget.text = "OFF"

    def change_way(self, widget):
        print("Switch:- ", widget.active)

    def on_text_validate(self, widget):
        self.text_input = widget.text


class MyApp(App):
    pass


MyApp().run()
