import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load.file("tela.kv")

class myapp(App):
    def build(self):
        return GUI