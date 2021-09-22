# Useful links:
# https://kivy.org/doc/stable/guide/basic.html#quickstart
# https://youtu.be/YDp73WjNISc

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Config.set('kivy', 'window_icon', '..\\Images/logo_ATTA_512.png')
Config.write()


class SayHello(App):

    def build(self):
        self.title = 'ATTA'
        self.window = GridLayout()

        # Styling the app:
        # Add margins to window
        self.window.size_hint = (0.9, 0.9)

        # Place window in the center
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Set the number of columns of GridLayout
        self.window.cols = 1

        # Add image widget
        self.window.add_widget(Image(source="..\\Images\\say_hello_small.png", allow_stretch=True))

        # Add label
        # Styling the label
        self.greeting = Label(text="What's your name?", font_size=18, color='#0cd3a7', bold=True)
        self.window.add_widget(self.greeting)

        # Text input widget
        # Styling the TextInput
        self.user = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 0.4))
        self.window.add_widget(self.user)

        # Button widget
        # Styling the button
        self.button = Button(text="GREET", size_hint=(1, 0.4), bold=True, background_color='#0cd3a7')

        # Connect callback function to a click event:
        self.button.bind(on_press=self.callback)

        self.window.add_widget(self.button)

        return self.window

    def callback(self, event):
        self.greeting.text = 'Hello ' + self.user.text + '!'


SayHello().run()
