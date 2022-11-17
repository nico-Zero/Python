from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


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
        self.speed_x = dp(10)
        self.speed_y = dp(10)

        with self.canvas:
            self.ball_size = dp(50)
            self.elip = Ellipse(
                pos=(0, 0),
                size=(self.ball_size, self.ball_size),
            )
        Clock.schedule_interval(self.update, 0.01)

    def on_size(self, *args):
        self.elip.pos = (
            self.center_x - self.ball_size / 2,
            self.center_y - self.ball_size / 2,
        )

    def update(self, dt):
        x, y = self.elip.pos

        if x > self.width - self.ball_size:
            self.speed_x *= -1
            self.elip.pos = (self.width, y)
        elif x < 0:
            self.speed_x *= -1
            self.elip.pos = (0, y)

        if y > self.height - self.ball_size:
            self.speed_y *= -1
            self.elip.pos = (x, self.height)
        elif y < 0:
            self.speed_y *= -1
            self.elip.pos = (x, 0)

        self.elip.pos = (x + self.speed_x, y + self.speed_y)


class CanvasExample6(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def hello(self):
        print("Hello!")


class CanvasExample7(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):
    pass


MyApp().run()
