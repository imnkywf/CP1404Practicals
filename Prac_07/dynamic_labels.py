from kivy.app import App
from kivy.lang import Builder

class Label(App):
    def build(self):
        self.title = "Square Number"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

Label().run()