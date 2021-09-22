# Useful links:
# https://kivy.org/doc/stable/guide/basic.html#quickstart
# https://kivy.org/doc/stable/api-kivy.app.html
# https://youtu.be/YDp73WjNISc

from kivy.app import App
from kivy.uix.label import Label


# The MyMainApp() class is derived from the App() class of the kivy.app repository.
# The App() class is the base for creating Kivy applications.

# Kivy requires that the class inherits from the App class
class MyApp(App):

    # The build() method initializes the application and returns a widget that will be used as [root] and added to the window.
    # This method doesn't need to be called,: the App().run() will do that.
    def build(self):
        label = Label(text="Hello World")
        return label


if __name__ == "__main__":
    MyApp().run()
