########################
## Team Members
## Name1:         
## Name2:
#########################

from tkinter import *
import random


class Dot:
    def __init__(self,canvas,x,y,color="rainbow",bool=False):
        items =["red", "green", "blue", "yellow", "white", "orange", "purple"]
        self.canvas = canvas
        self.x = x
        self.y = y
        if color == 'rainbow':
            color = random.choice(items)
        self.color = color
        dot = self.canvas.create_oval(self.x,self.y,self.x+2,self.y+2, fill = self.color, outline = self.color)
        #print(self.x,self.y,color)
        self.dot = dot












        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

