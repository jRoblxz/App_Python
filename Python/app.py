import kivy
from kivy.app import App
from kivy.lang import Builder

# Load the KV file
Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return Builder.load_file("tela.kv")

if __name__ == "__main__":
    MyApp().run()
