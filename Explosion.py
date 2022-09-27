from tkinter import *
import math,time,random
from Dot import Dot
import numpy as np


class Explosion:
    def __init__(self, canvas, radius=80, color="rainbow", layers=15):
        dots = []
        self.radius = radius
        self.color = color
        self.layers = layers
        self.dots = dots
        self.canvas = canvas
        active = False
        self._active = active
    
    def activate(self,x,y):
        self.x = x
        self.y = y
        self.r = 0
        self._active = True

    def is_active(self):
        return self._active
    
    def deactivate(self):
        for dot in self.dots:
            self.canvas.delete(dot.dot)
        self._active = False
    
    def next(self):
        if self._active:
            self.r += 1
            if self.r > self.radius:
                self.deactivate()
            else:
                for layer in range(self.layers):
                    angle = random.randint(0,359)
                    if angle <= 90:
                        angle_rad = angle * math.pi/180
                        x = self.x + self.r * math.cos(angle_rad)
                        y = self.y - self.r * math.sin(angle_rad)
                    elif angle > 90 and angle <= 180:
                        angle_rad = (180-angle) * math.pi/180
                        x = self.x - self.r * math.cos(angle_rad)
                        y = self.y - self.r * math.sin(angle_rad)
                    elif angle > 180 and angle <= 270:
                        angle_rad = (angle-180) * math.pi/180
                        x = self.x - self.r * math.cos(angle_rad)
                        y = self.y + self.r * math.sin(angle_rad)
                    elif angle > 270 and angle<=359:
                        angle_rad = (359-angle) *math.pi/180
                        x = self.x + self.r * math.cos(angle_rad)
                        y = self.y + self.r * math.sin(angle_rad)
                    
                    dot = Dot(self.canvas,x,y,self.color)
                    self.dots.append(dot)


    @staticmethod
    def add_explosion(canvas, booms, center_x, center_y, max_size=80, color = "rainbow"):
        to_remove = []

        explosion_picker = [Explosion(canvas, max_size, color), Explosion_gravity(canvas, max_size, color)]
        boom = explosion_picker[random.randint(0,1)]
        Explosion.activate(boom, center_x, center_y)

        for i in range(len(booms)):
            if not booms[i].is_active():
                to_remove.append(i)
        to_remove.reverse()
        for i in to_remove:
            booms.pop(i)
        
        booms.append(boom)

class Explosion_gravity(Explosion):
    def __init__(self, canvas, radius=80, color="rainbow", layers=15):
        super().__init__(canvas, radius, color, layers)

        self.theta = np.zeros(self.layers)
        self.speed = np.zeros(self.layers)

        for i in range(self.layers):
            self.theta[i] = np.random.randint(0,359) * math.pi/180
            self.speed[i] = np.random.randint(1,5)
        
    def next(self):
        if self._active:
            self.r +=1
            g = 0.06

            if self.r > self.radius:
                    self.deactivate()
            else:
                for layer in range(self.layers):
                    x = self.x - self.speed[layer] * math.cos(self.theta[layer]) * self.r
                    y = self.y - self.speed[layer] * math.sin(self.theta[layer]) * self.r + g/2 * self.r**2

                    dot = Dot(self.canvas,x,y,self.color)
                    self.dots.append(dot)



                    
            


#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y))

        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

