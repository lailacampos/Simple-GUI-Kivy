# Useful links
# https://youtu.be/xaYn4XdieCs

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        # Now Kivy will associate the my.kv file with MyMainApp class
        return kv


# Insert a file into the language builder and return the root widget (if defined) of the kv file.
kv = Builder.load_file("my.kv")

if __name__ == '__main__':
    MyMainApp().run()
