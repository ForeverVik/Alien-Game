from tkinter import *

class SpaceShip:
    def __init__(self,canvas):
        self.canvas = canvas 
        self.__active = False
    def activate(self):
        self.xtracker = self.canvas.winfo_width()*0.5
        self.active = True
        self.shippic=PhotoImage(file="ship.png")
        self.y = self.canvas.winfo_height()-(self.shippic.height())*1.3
        self.ship = self.canvas.create_image(self.canvas.winfo_width()*0.5, self.y, image = self.shippic)
    def deactivate(self):
        self.canvas.delete(self.ship)
    def is_active(self):
        return self.active
    def shift_left(self):
        if self.xtracker > 45:
            self.xtracker =  self.xtracker - 15
            self.canvas.move(self.ship,-15,0)
        else:
            pass
    def shift_right(self):
        if self.xtracker < (self.canvas.winfo_width()-45):
            self.xtracker =  self.xtracker + 15
            self.canvas.move(self.ship,15,0)
        else:
            pass


 

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

