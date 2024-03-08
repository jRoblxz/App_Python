import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.lang import builder

GUI = builder.load.file("tela.kv")

class myapp(App):
    def build(self):
        return GUI