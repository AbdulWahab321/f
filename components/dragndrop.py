class DragManager():
    def __init__(self,on_drag_start_callback=None,on_drag_motion_callback=None):
        self.odsc = on_drag_start_callback
        self.odmc = on_drag_motion_callback
    def make_draggable(self,widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)
    
    def on_drag_start(self,event):
        if event!=None:
            widget = event.widget
            widget._drag_start_x = event.x
            widget._drag_start_y = event.y 
            if self.odsc:self.odsc()

    def on_drag_motion(self,event):
        if event!=None:
            widget = event.widget
            x = widget.winfo_x() - widget._drag_start_x + event.x
            y = widget.winfo_y() - widget._drag_start_y + event.y
            widget.place(x=x, y=y) 
            if self.odmc:self.odmc()  