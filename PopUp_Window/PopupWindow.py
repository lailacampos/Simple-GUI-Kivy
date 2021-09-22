# Useful links:
# https://youtu.be/PpLuyOzCKTQ

# Answer about closing a popup by clicking a button:
# https://stackoverflow.com/q/60897642/11627241

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class Widgets(Widget):

    @staticmethod
    def onPressButton():
        show_popup()


class MyPopup(FloatLayout):
    popup = ObjectProperty(None)


class MyApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = MyPopup()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))
    show.popup = popupWindow
    popupWindow.open()


if __name__ == '__main__':
    MyApp().run()
