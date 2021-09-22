# Useful links:
# https://youtu.be/yg7n8hP6k1w

from kivy.app import App
from kivy.uix.widget import Widget


class Touch(Widget):
    def on_touch_up(self, touch):
        print('Mouse Up', touch)

    def on_touch_down(self, touch):
        print('Mouse down', touch)

    def on_touch_move(self, touch):
        print('Mouse move', touch)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()
