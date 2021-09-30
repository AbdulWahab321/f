from components import *        
from tkinter.ttk import *
import keyboard

app = App("GUI Engine")

btn = app.createNewItem("button","My Button",YPos(360),image="components/assets/ntpd.png")
input = app.createNewItem("input","My Button",YPos(250))
app.create_splitLine()

app.run()