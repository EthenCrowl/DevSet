from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.extras.highlight import KivyLexer
from kivy.extras.highlight import CythonLexer

class SimpleKivy(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    SimpleKivy().run()
