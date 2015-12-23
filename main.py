import os
import sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RootWidget(BoxLayout):
    pass

class DevSetApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DevSetApp().run()