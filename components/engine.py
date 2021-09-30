import tkinter.ttk
from tkinter.ttk import *
import tkinter
try:
    from simplifier import *
except:
    from .simplifier import *
class Popup_Editor:
    def __init__(self,widgetname:str="Button"):
        self.tow = widgetname.lower().capitalize()
        screen_title = f"{self.tow} Editor"
        self.root = tkinter.Tk()
        self.root.state('zoomed')   
        self.root.title(screen_title)     
        self.styleOption = Style(self.root)
        self.styleOption.theme_use("vista")
    def on_change_input(self,change_callback=None):
        self.change_callback = change_callback     
    def AX_pos(self,position):
        return AXPos(self.root,position) 
    def AY_pos(self,position):
        return AYPos(self.root,position) 
    def set_input(self):
        x = self.x.get_value()
        y = self.y.get_value()
        self.data = {"x":x,"y":y}
    def get_data(self):
        return self.data    
    def createLE(self,Ypos=350,label="x:"):
        self.sv = tkinter.StringVar(self.root)
        SV = self.sv
        ROOT = self.root
        AX_pos = self.AX_pos
        AY_pos = self.AY_pos
        set_data = self.set_input
        change_callback = self.change_callback
        class LE:
            def __init__(self):
                mainX = 650
                mainY = Ypos
                self.inp = Entry(ROOT,width=25,textvariable=SV)
                self.inp.place(x=AX_pos(mainX),y=AY_pos(mainY))
                lx = Label(ROOT,text=label,font=(None,15))
                lx.place(x=AX_pos(mainX+15),y=AY_pos(mainY+5)) 
                SV.trace("w",lambda name, index, mode,callback=change_callback:self.OnChangecallback(name,index,mode,callback))      
            def get_value(self):
                return self.inp.get()
            def get_input(self):
                return self.inp
                     
            def OnChangecallback(self,name, index, mode,callback):
                set_data()
                change_callback() if change_callback else None
         
                   
        le = LE()                         
           
        return le         
    def show(self):
        tow = self.tow.lower()
        if tow == "btn" or tow == "button":
            self.x = self.createLE()
            self.y = self.createLE(320,"y:")
            

        self.root.mainloop()        

pe = Popup_Editor()
pe.on_change_input(lambda:print(pe.get_data()))
pe.show()