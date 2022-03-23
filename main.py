import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.myWindow = None
        self.image1 = None
        self.label1 = None
        self.textinput1 = None
        self.button1 = None

    def build(self):
        self.myWindow = GridLayout()
        self.myWindow.cols = 1

        # styling windows

        self.myWindow.size_hint = (0.5, 0.5)
        self.myWindow.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.image1 = Image(source="logo.png")
        self.myWindow.add_widget(self.image1)

        self.label1 = Label(text='Whats your name?',
                            font_size=18,
                            color='#00FFCE')
        self.myWindow.add_widget(self.label1)

        self.textinput1 = TextInput(multiline=False,
                                    padding_y=(10, 10),
                                    size_hint=(1, 0.5))
        self.myWindow.add_widget(self.textinput1)

        self.button1 = Button(text='GREET',
                              size_hint=(1, 0.5),
                              bold=True,
                              background_color='#00FFCE')
        self.button1.bind(on_press=self.callback)
        self.myWindow.add_widget(self.button1)

        return self.myWindow

    def callback(self, instance):
        self.label1.text = "hello " + self.textinput1.text + "!"


if __name__ == '__main__':
    MyApp().run()
