# Useful links:
# https://youtu.be/lnOTAq4NQfQ
# https://kivy.org/doc/stable/api-kivy.uix.floatlayout.html#module-kivy.uix.floatlayout
# https://kivy.org/doc/stable/guide/widgets.html
# https://kivy.org/doc/stable/api-kivy.uix.floatlayout.html#kivy.uix.floatlayout.FloatLayout

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    MyApp().run()
