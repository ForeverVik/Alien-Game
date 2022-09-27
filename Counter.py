from tkinter import *

class Counter:
    def __init__(self,canvas,initial_value=0): # constructor
        self.canvas = canvas
        self.value = initial_value

        self.create_text()

    def increment(self,increment):
        # delete old score value to prevent text overlap and redraw based on input given
        self.canvas.delete(self.current_score)
        self.value = self.value + increment
        self.current_score = self.canvas.create_text(self.canvas.winfo_width()-30,20,text=str(self.value),fill="orange",font=("Courier",25))

    def create_text(self):
        # draw the intial score value, 0 by default
        self.current_score = self.canvas.create_text(self.canvas.winfo_width()-30,20,text=str(self.value),fill="orange",font=("Courier",25))
        
    def get_value(self):
        return int(self.value)




def main(): 
    ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas 
        canvas.pack()
        root.update() # update the graphic
        C = Counter(canvas,10) # instantiate the class Counter
        root.bind("<Right>",lambda e:C.increment(1))
        root.bind("<Left>",lambda e:C.increment(-1))
        root.update()   # update the graphic
        root.mainloop()





if __name__=="__main__":
    main()



        
