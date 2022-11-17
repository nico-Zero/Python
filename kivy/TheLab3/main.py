from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from time import sleep


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            for i in range(1, 200, 2):
                Line(points=(1 * i, 1 * i, 4 * i, 5 * -i))
                Color(1, 1, 1)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(400, 200, 100, 200))
            self.rect = Rectangle(pos=(200, 400), size=(100, 100))

    def on_button_click(self, condition):
        x, y = self.rect.pos
        w, h = self.rect.size
        print(x, y)
        print(self.width, self.height)
        if 0 < x < self.width - w and 0 < y < self.height - h:
            if condition:
                self.rect.pos = (self.rect.pos[0] + 10, 400)
            else:
                self.rect.pos = (self.rect.pos[0] - 10, 400)
        else:
            if x == 0:
                self.rect.pos = (self.rect.pos[0] + 10, 400)
            else:
                self.rect.pos = (self.rect.pos[0] - 10, 400)

    def auto_run(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        while 1:

            pass


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.size)
        with self.canvas:
            self.ball_size = dp(50)
            self.elip = Ellipse(
                pos=(0, 0),
                size=(self.ball_size, self.ball_size),
            )
        Clock.schedule_interval(self.update, 1)

    def on_size(self, *args):
        self.elip.pos = (
            self.center_x - self.ball_size / 2,
            self.center_y - self.ball_size / 2,
        )

    def update(self, dt):
        print("update")
        speed_x = dp(10)
        speed_y = dp(10)
        x, y = self.elip.pos

        if 0 > x > self.width:
            speed_x *= -1
        if 0 > y > self.height:
            speed_y *= -1

        self.elip.pos = (x + speed_x, y + speed_y)


class MyApp(App):
    pass


MyApp().run()
