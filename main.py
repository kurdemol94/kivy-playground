from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class TutorialApp(App):
    def build(self):
        defaultText = 'enter your text here'
        floatLayout = FloatLayout()
        textInput = TextInput(font_size=150, size_hint_y=None, height=200, text=defaultText)
        boxLayout = BoxLayout(orientation='vertical')
        scatter = Scatter()        
        label = Label(text=defaultText)

        textInput.bind(text=label.setter('text'))

        floatLayout.add_widget(scatter)
        scatter.add_widget(label)


        boxLayout.add_widget(textInput)
        boxLayout.add_widget(floatLayout)
        return boxLayout
    

if __name__ == "__main__":
        TutorialApp().run()
