# ---------- KIVYTUT.PY ----------
 
# It is common practice to create your own custom
# widgets so base widgets aren't effected
''' 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.widget import Widget
 
class CustomWidget(Widget):
    pass
 
class CustomWidgetApp(App):
 
    def build(self):
        return CustomWidget()
 
customWidget = CustomWidgetApp()
 
customWidget.run()


 
# ---------- KIVYTUT2.PY ----------

import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
 
# A Float layout positions and sizes objects as a percentage
# of the window size
 
class FloatingApp(App):
 
    def build(self):
        return FloatLayout()
 
flApp = FloatingApp()
 
flApp.run()
 
'''
 
# ---------- KIVYTUT3.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
 
# The Grid Layout organizes everything in a grid pattern
 
class GridLayoutApp(App):
 
    def build(self):
        return GridLayout()
 
glApp = GridLayoutApp()
 
glApp.run()
 
'''
# ---------- KIVYTUT4.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
 
# With a box layout we arrange widgets in a horizontal
# or vertical box
 
class BoxLayoutApp(App):
 
    def build(self):
        return BoxLayout()
 
blApp = BoxLayoutApp()
 
blApp.run()
 
 
# ---------- KIVYTUT5.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
 
# A stack layout arranges widgets vertically or horizontally
# as they best fit
 
class StackLayoutApp(App):
 
    def build(self):
        return StackLayout()
 
slApp = StackLayoutApp()
 
slApp.run()
 

 
# ---------- KIVYTUT6.PY ----------
 
import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
 
# A page layout is used to create multi-page layouts
# that you can flip through
 
class PageLayoutApp(App):
 
    def build(self):
        return PageLayout()
 
plApp = PageLayoutApp()
 
plApp.run()
'''
