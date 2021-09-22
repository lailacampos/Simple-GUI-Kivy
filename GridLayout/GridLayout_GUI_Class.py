# Useful links:
# https://realpython.com/python-kwargs-and-args/
# https://youtu.be/fGWHQA3LhJ8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        # Inner GridLayout
        self.innerGrid = GridLayout()
        self.innerGrid.cols = 2

        self.innerGrid.add_widget(Label(text="First Name:"))
        self.firstName = TextInput(multiline=False)
        self.innerGrid.add_widget(self.firstName)

        self.innerGrid.add_widget(Label(text="Last Name:"))
        self.lastName = TextInput(multiline=False)
        self.innerGrid.add_widget(self.lastName)

        self.innerGrid.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.innerGrid.add_widget(self.email)

        self.add_widget(self.innerGrid)

        self.button = Button(text="Submit", font_size=20)
        self.button.bind(on_press=self.onPress)
        self.add_widget(self.button)

    def onPress(self, instance):
        name = self.firstName.text
        lastName = self.lastName.text
        email = self.email.text

        print('Name: ' + name)
        print('Surname: ' + lastName)
        print('Email: ' + email)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()