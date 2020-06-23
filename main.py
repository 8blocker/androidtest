from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="PRINCESS", font_size = 150)

        f.add_widget(s)
        s.add_widget(l)
        return f
if __name__ == "__main__":
    MyApp().run()