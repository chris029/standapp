from kivy.clock import Clock
from time_guard import TimeGuard
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

timer = TimeGuard(1)

Builder.load_file('StandApp.kv')

class AnotherScreen(Screen):
    pass



class ScreenManagement(ScreenManager):
    pass



class Container(Screen):
    def AssignTime(self):
        timer.setTimeInt(self.ids.timeInput.text)



class StandApp(App):

    def build(self):
        self.title = 'StandApp'
        Clock.schedule_interval(lambda dt: self.my_callback(), 10)

        return ScreenManagement()

    def my_callback(self):
        app = App.get_running_app()

        timer.CheckTime()
        if(isinstance(app.root.current_screen, Container)):
            if(timer.getStatus()):
                app.root.current = 'other'



def main():
    app = StandApp()
    app.run()

if __name__ == '__main__':
    main()
