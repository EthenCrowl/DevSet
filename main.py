import os
import sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from kivy.app import App


class DevSet(App):
    pass


if __name__ == '__main__':
    DevSet().run()
