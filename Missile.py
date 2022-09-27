from tkinter import *
import time,random

class Missile:
    def __init__(self, canvas, ceiling=0, pixel_increment=5, color="orange", width=8, height=25):
        __active = False
        self.__active = __active
        self.canvas = canvas
        self.ceiling = ceiling
        self.increment = pixel_increment
        self.color = color
        self.width = width
        self.height = height

    def activate(self, x, y):
        self.x = x
        self.y = y
        self.__active = True
        self.missile = self.canvas.create_rectangle(self.x-(0.5*self.width), self.y+self.height, self.x+(0.5*self.width), self.y, fill=self.color)
    
    def deactivate(self):
        self.canvas.delete(self.missile)
        self.__active = False
    
    def is_active(self):
        return self.__active

    def next(self):
        if self.__active:
            self.canvas.move(self.missile, 0, -self.increment)
            self.y -= self.increment
            if self.y < self.ceiling:
                Missile.deactivate(self)
    
    @staticmethod
    def add_missile(canvas, missile_list, start_x, start_y, max_height=0, pixel_increment=5, color="orange"):
        to_remove = []

        missile = Missile(canvas, max_height, pixel_increment, color)
        Missile.activate(missile, start_x, start_y)

        for i in range(len(missile_list)):
            if not missile_list[i].is_active():
                to_remove.append(i)
        to_remove.reverse()
        for i in to_remove:
            missile_list.pop(i)

        missile_list.append(missile)



###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        colors =["red", "green", "blue", "yellow", "orange", "purple"]

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock       
        while True:
            for missile in missiles:
                missile.next()
            
            if t%50 == 0:
                rand_x = random.uniform(0, w)
                rand_ceiling = random.uniform(0, h)
                random_speed = random.uniform(0,7)
                random_color = colors[random.randint(0, len(colors)-1)]
                Missile.add_missile(canvas, missiles, rand_x, h, rand_ceiling, pixel_increment=random_speed, color= random_color)




           ##### To complete








            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(),end=" ")
            print()
            
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

