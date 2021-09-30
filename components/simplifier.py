def get_x_pos(widget):
    return widget.winfo_x()
def get_y_pos(widget):
    return widget.winfo_y() 
def get_width(widget):
    return widget.winfo_width()
def get_height(widget):
    return widget.winfo_height()
def get_widgetType(widget):
    tow = str(type(widget)).replace("<class","").replace(">","").replace(" ","").replace("'","").replace("tkinter.ttk.","").lower().strip()
    return tow
class CollisionWidgets:
    def __init__(self,widget1,widget2):
        self.w1 = widget1
        self.w2 = widget2
        self.x1 = get_x_pos(self.w1)
        self.x2 = get_x_pos(self.w2)
        
        self.y1 = get_y_pos(self.w1)
        self.y2 = get_y_pos(self.w2)
        
        self.ww1 = get_width(self.w1)
        self.ww2 = get_width(self.w2)
        
        self.hw1 = get_height(self.w1)
        self.hw2 = get_height(self.w2)
    def isColliding(self):
        x1, y1 = get_x_pos(self.w1), get_y_pos(self.w1)
        width1, height1 = get_width(self.w1), get_height(self.w1)
        
        x2, y2 = get_x_pos(self.w2), get_y_pos(self.w2)
        width2, height2 = get_width(self.w2), get_height(self.w2)    
        
        if x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2:
            return True
        else:
            return False
    def collide_widget1(self):
        hw2 = self.hw2*26
        self.w2.place(x=self.x1 + self.ww2*43,y=self.y1 + hw2)
    def collide_widget2(self):
        hw1 = self.hw1*26
        self.w1.place(x=self.x2 + self.ww1*43,y=self.y2 + hw1)                   
    def destroy_widget1(self):
        self.w1.destroy()    
    def destroy_widget2(self):
        self.w2.destroy()
    def destroy_all(self):
        self.destroy_widget1()
        self.destroy_widget2()
            
def YPos(position):
    
    import ctypes
    monitor_height = ctypes.windll.user32.GetSystemMetrics(1)
    return monitor_height // 2 - position 
def XPos(position):
    import ctypes
    monitor_width = ctypes.windll.user32.GetSystemMetrics(0)
    return monitor_width // 2 - position         
def AXPos(root,position):
    import ctypes
    sw = str(get_width(root))
    if sw == "1":sw = ctypes.windll.user32.GetSystemMetrics(0)
    else:sw = sw
    return sw // 2 - position

def AYPos(root,position):
    import ctypes
    sh = str(get_height(root))  
    if sh == "1" or sh == "0":sh = ctypes.windll.user32.GetSystemMetrics(1)
    else:sh = sh      
    return sh // 2 - position
class Tracker:
    """ Toplevel windows resize event tracker. """

    def __init__(self, toplevel,callback):
        self.toplevel = toplevel
        self.clb = callback
        self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
        self._func_id = None

    def bind_config(self):
        self._func_id = self.toplevel.bind("<Configure>", self.resize)

    def unbind_config(self):  # Untested.
        if self._func_id:
            self.toplevel.unbind("<Configure>", self._func_id)
            self._func_id = None
    def get_winWidth(self):
        return self.width
    def get_winHeight(self):
        return self.height
    def resize(self, event):
        if(event.widget == self.toplevel and
           (self.width != event.width or self.height != event.height)):
            self.width, self.height = event.width, event.height     
            if self.clb:self.clb() 
                  