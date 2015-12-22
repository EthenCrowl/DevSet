import os
import sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior


class DevSetApp(App):
    pass


if __name__ == '__main__':
    DevSetApp().run()
