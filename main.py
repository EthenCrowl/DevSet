from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer
from pygments.lexers.python import Python3Lexer

class Python3CodeInput(CodeInput):
    def build(self):
        return CodeInput(lexer=Python3Lexer())

class SimpleKivy(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    SimpleKivy().run()
