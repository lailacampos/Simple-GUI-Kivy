# Useful links:
# https://youtu.be/8vD-V5jpjBo

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Rectangle


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:

            Color(0, 1, 0, 0.5, mode='rgba')
            # https://kivy.org/doc/stable/api-kivy.graphics.html?highlight=graphics#kivy.graphics.Line
            Line(points=[100, 100, 100, 500, 200, 200])

            # https://kivy.org/doc/stable/api-kivy.graphics.html?highlight=graphics#kivy.graphics.Color
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rectangle = Rectangle(pos=(0, 0), size=(150, 150))

    def on_touch_down(self, touch):
        self.rectangle.pos = touch.pos

    def on_touch_move(self, touch):
        self.rectangle.pos = touch.pos


class MyDrawingApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    MyDrawingApp().run()
