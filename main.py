from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="Hello from Kivy on GitHub!", font_size='24sp')

if __name__ == '__main__':
    TestApp().run()