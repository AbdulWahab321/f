from tkinter import Tk
from tkinter.ttk import *
from .dragndrop import DragManager


class DraggableButton:
    def __init__(self,root=None,text="",clickCallbackFunction=None):
        self.root = None
        self.callback = clickCallbackFunction
        self.text = text
        
        if root:
            self.root = root
        else:
            self.root = Tk() 
    def get_x_pos(self):
        return self.btn.winfo_x()
    def get_y_pos(self):
        return self.btn.winfo_y()    
                      
    def create(self,on_drag_start_callback=None,on_drag_motion_callback=None):        
        if self.callback:self.btn = Button(self.root,text=self.text,command=self.callback)
        else:self.btn = Button(self.root,text=self.text)
        self.btn.config(takefocus=False)
        self.btn.pack()
        self.dgMnger = DragManager(on_drag_start_callback,on_drag_motion_callback)
        self.dgMnger.make_draggable(self.btn)
        
        return self.btn 
class DraggableWidgetMaker:
    def __init__(self):
        pass
    def create(self,widget,on_drag_start_callback=None,on_drag_motion_callback=None):
        self.widget = widget
        self.dgMnger = DragManager(on_drag_start_callback,on_drag_motion_callback)
        self.dgMnger.make_draggable(self.widget)
    def get_x_pos(self):
        return self.widget.winfo_x()
    def get_y_pos(self):
        return self.widget.winfo_y()                