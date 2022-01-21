from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest

class TrovaTemperatura(Screen):
    label = ObjectProperty(None)
    input_text: ObjectProperty(None)

    def __init__(self):
        super(TrovaTemperatura, self).__init__()
        self.size_hint = (0.8, 0.9)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def search_temp(self): 
        link = f'https://api.openweathermap.org/data/2.5/weather?q={self.input_text.text}&appid=44cf138b8e86e5cd86f78f51024bd171&units=metric'
        UrlRequest(link, self.update_label)
        
    def update_label(self, req, result):
        temp = result['main']['temp']
        self.label.text = f'Attualmente a {self.input_text.text} fanno {temp} °C'
        
class Applicazione(App):
    def build(self):
        Window.clearcolor = (0.654, 0.698, 0.933, 0)
        Window.size = (360, 640)
        return TrovaTemperatura()

Applicazione().run()