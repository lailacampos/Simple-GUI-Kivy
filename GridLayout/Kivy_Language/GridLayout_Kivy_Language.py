# https://youtu.be/AS3b70pLYEU
# Kivy Language:
# https://kivy.org/doc/stable/guide/lang.html


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):

    # Object is initialized to None
    # Variables names need to be the same as in the .kv file
    firstName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def onPressButton(self):
        print('Name: ', self.firstName.text)
        print('Surname: ', self.lastName.text)
        print('Email: ', self.email.text)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
