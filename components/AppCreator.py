from tkinter import Tk
from tkinter.ttk import *
from .simplifier import *
from .draggableButton import DraggableWidgetMaker
import tkinter
import ctypes

monitor_width, monitor_height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
class App(Frame):
    def __init__(self,window_title=None):
        
        if window_title:self.root = Tk(screenName=window_title)
        super().__init__(master=self.root)
        self.root.state('zoomed')
        self.widgetMargin = self.get_window_width() // 2 + 250   
        self.init_Ui()
    def init_Ui(self):
        self.pack(fill=tkinter.BOTH, expand=1)

        self.canvas = tkinter.Canvas(self)  
        self.canvas.pack(fill=tkinter.BOTH, expand=1)  
    def createVerticalLine(self,x,startPointY,endPointY):
        ln = None
        def recreate():
            global ln
            try:
                self.canvas.delete(ln)
            except:
                pass
            ln = self.canvas.create_line(x, startPointY, x, endPointY)
        ln = self.canvas.create_line(x, startPointY, x, endPointY)
        tck = Tracker(self.root,lambda:recreate())
        tck.bind_config()
    def create_splitLine(self):
        self.createVerticalLine(self.widgetMargin,0,800)    
    def createHorizontalLine(self,y,startPointX,endPointX):
        ln = None
        def recreate():
            global ln
            self.canvas.delete(ln)
            self.canvas.create_line(startPointX, y, endPointX, y)        
        self.canvas.create_line(startPointX, y, endPointX, y)
        tck = Tracker(self.root,lambda:recreate())
        tck.bind_config()
    def return_canvas(self):
        return self.canvas    
    def return_root(self):
        return self.root          
    def useStyle(self,custom_theme="vista"):
        self.style = Style(self.root)
        self.style.theme_use(custom_theme)           
    def checkXandY(self,widget):
        x,y = get_x_pos(widget), get_y_pos(widget)
        width,height = get_width(widget), get_height(widget)
        
        window_width, window_height = get_width(self.root), get_height(self.root)
        
        
                    
    def createLabel(self,master=None,text="",font="Consolas",fontsize=35,packORplace="pack",padx=None,pady=None,x=None,y=None):
        lbl = Label(master if master else self.root,text=text,font=(font,fontsize))
        if packORplace == "pack":
            lbl.pack(padx=padx,pady=pady)
        else:
            lbl.place(x=x,y=y)  
    def get_window_height(self):
        return self.root.winfo_height()
    def get_window_width(self):
        return self.root.winfo_width()     
    def focus_on(self,widget):
        tow = ""
        if get_x_pos(widget) < self.widgetMargin:
            pass
        else:      
            tow = str(type(widget)).replace("<class","").replace(">","").replace(" ","").replace("'","").replace("tkinter.ttk.","").lower().strip()
            if tow == "button":
                print("Focusing on a Button") 
    def bindRightClick(self,widget):
        m = tkinter.Menu(self.root, tearoff = 0)
        m.add_command(label ="Open Editor Tools",command=lambda:self.focus_on(widget))
        
        def do_popup(event):
            if get_x_pos(widget) > self.widgetMargin:    
                try:
                    m.tk_popup(event.x_root, event.y_root)
                finally:
                    m.grab_release()         

        widget.bind("<Button-3>", do_popup)        
               
    def createNewItem(self,widget:str="button",text:str="widget",yposition:int=50,width:int=15,height:int=None,image=None):
        widget = widget.lower()
        current_win_height = None
        if self.get_window_height() == 1:
            current_win_height = monitor_height
        else:
            current_win_height = self.get_window_height()
          
            
        if widget == "button":
            if image!=None:
                img = tkinter.PhotoImage(file=image,name="image",master=self.root)
                img.configure(width=25,height=25)
                btn = Button(self.root,width=width,height=height,takefocus=False,text=text if text else None,image=img,compound="left")
            else:
                btn = Button(self.root,width=width,height=height,takefocus=False,text=text if text else None)
            btn.configure(command=lambda:self.focus_on(btn))
            dgm = DraggableWidgetMaker()
            btn.place(x=self.get_window_width() // 2 + 45, y = yposition)
            tck = Tracker(self.root,btn.place(x=self.get_window_width() // 2 + 45, y = yposition))
            tck.bind_config()
            dgm.create(btn,None,lambda:self.checkXandY(btn))
            self.bindRightClick(btn)
            return btn  
        elif widget == "input":
            inp = Entry(self.root,width=width+1,height=height,textvariable=text if text else None)
            dgm = DraggableWidgetMaker()
            inp.place(x=self.get_window_width() // 2 + 45, y = yposition)
            tck = Tracker(self.root,inp.place(x=self.get_window_width() // 2 + 45, y = yposition))
            tck.bind_config()
            dgm.create(inp,None,lambda:self.checkXandY(btn))      
            return inp 
              
        
    def run(self):
        self.root.mainloop()
        