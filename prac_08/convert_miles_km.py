from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.60934


class ConvertMilesApp(App):
    result_text = StringProperty('')

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0

        miles += value
        self.root.ids.miles_input.text = str(miles)
        self.calculate_conversion()

    def handle_input_change(self):
        self.calculate_conversion()

    def handle_convert(self):
        self.calculate_conversion()

    def calculate_conversion(self):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0

        kilometers = miles * MILES_TO_KM_FACTOR
        self.result_text = f'Result: {kilometers:.2f} km'


if __name__ == '__main__':
    ConvertMilesApp().run()
