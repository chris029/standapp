from time_guard import TimeGuard
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass
    
class StandApp(App):

    def build(self):
        self.title = 'StandApp'
        return Container()

def main():
    app = StandApp()
    app.run()
    
    
if __name__ == '__main__':
    main()