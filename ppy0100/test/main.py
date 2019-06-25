import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
kivy.require('1.8.0')
class RootWidget(BoxLayout):
    container=ObjectProperty(None)
class EzApp(App):
    def build(self):
        self.root=Builder.load_file('kv/1.kv')
app=EzApp()
app.run()