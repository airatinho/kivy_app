from  kivymd.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy','keyboard_mode','systemanddoc')
Window.size=(480,853)


def get_ing(mas):
    nitr=str(10*mas/1000)
    sald=str(15*mas/1000)
    start=str(0.5*mas/1000)
    sugars=str(5*mas/1000)
    time_v=str(round(mas / 500*2))
    return {"nitro":nitr,"sald":sald,"start":start,"sugars":sugars,"time_v":time_v}


class Container(GridLayout):

    def calculate(self):
        try:
            mas = int(self.text_input.text)
        except Exception:
            mas= 0

        ingredients = get_ing(mas)
        self.sald.text=ingredients['sald']+ ' +5'
        self.nitr.text=ingredients['nitro']
        self.sugars.text = ingredients['sugars']
        self.start.text = ingredients['start']
        self.time_v.text = ingredients['time_v']

class MyApp(App):
    def build(self):

        return Container()

if __name__ == '__main__':
    MyApp().run()