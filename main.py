import kivy
kivy.require("1.11.1") # set version
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder


class MyCustomBoxLayout(BoxLayout):
    def custom_callback(self):
        print("Custom callback called.")


class MyApp(App):
    def build(self):
        return Builder.load_file('example.kv')


if __name__ == "__main__":
    MyApp().run()
