from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Explicitly load the KV file
Builder.load_file("musicapp.kv")

class MusicApp(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MusicApp()

if __name__ == "__main__":
    MainApp().run()
