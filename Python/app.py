import kivy
kivy.require('2.1.0')  # substitua pela sua versão atual do kivy!

from kivy.app import App
from kivy.lang import Builder

class MyApp(App):
    def build(self):
        return Builder.load_file("style.kv")

    def button_click(self):
        print("EU TE AMO")


if __name__ == "__main__":
    MyApp().run()
