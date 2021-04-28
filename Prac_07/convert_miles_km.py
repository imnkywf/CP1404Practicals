from kivy.app import App
from kivy.lang import Builder

class Converter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        km = value * 1.60934
        self.root.ids.output_label.text = str(km)

    def handle_change(self, change):
        result = float(self.root.ids.input_number.text) + change
        self.root.ids.input_number.text = str(result)
        self.handle_calculation(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0



Converter().run()



