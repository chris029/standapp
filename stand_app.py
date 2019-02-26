from kivy.clock import Clock
from time_guard import TimeGuard
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

timer = TimeGuard(1)

Builder.load_file('StandApp.kv')

class Container(BoxLayout):
    def AssignTime(self):
        timer.setTimeInt(self.ids.timeInput.text)
        self.ids.animation.text = "Not yet"
        
class StandApp(App):

    def build(self):
        self.title = 'StandApp'
        Clock.schedule_interval(lambda dt: self.my_callback(), 10)
        
        return Container()
     
    def my_callback(self):
        app = App.get_running_app()
        
        timer.CheckTime()
        if(timer.getStatus()):
            app.root.ids.animation.text = "Yeah, it works"
        else:
            app.root.ids.animation.text = "Not yet"
            
def main():
    app = StandApp()
    app.run()
        
if __name__ == '__main__':
    main()
