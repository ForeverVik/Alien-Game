from tkinter import *
import math
import time, random

class Alien:
    def __init__(self, canvas, increment=4, color="yellow", w=50, h=50, value=1):
        self._active = False
        self.canvas = canvas
        self.increment = increment
        self.color = color
        self.w = w
        self.h = h
        self.value = value
    
    def activate(self, x=None, y=None):
        if x == None and y == None:
            self.x = random.randint(0, self.canvas.winfo_width())
            self.y = 0

            self.x1 = self.x - self.w/2
            self.x2 = self.x + self.w/2
            self.y1 = self.y - self.h/2
            self.y2 = self.y + self.h/2

            self._active = True

            self.alien = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
    
    def is_active(self):
        return self._active
    
    def deactivate(self):
        self.canvas.delete(self.alien)
        self._active = False

    def next(self):
        if self._active == True:
            self.y1 += self.increment
            self.y2 += self.increment

            self.y += self.increment

            self.canvas.move(self.alien, 0, self.increment)

            if self.y > self.canvas.winfo_height():
                self.deactivate()

    def is_shot(self, x, y):
        if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
            return True
        else:
            return False

    @staticmethod
    def add_alien(canvas, aliens):
        to_remove = []

        alien_picker = [Alien_red(canvas), Alien_blue(canvas), Alien_green(canvas), Alien_mine(canvas)]
        new_alien = alien_picker[random.randint(0,3)]
        new_alien.activate()

        for i in range(len(aliens)):
            if not aliens[i].is_active():
                to_remove.append(i)
        to_remove.reverse()
        for i in to_remove:
            aliens.pop(i)
        
        aliens.append(new_alien)



class Alien_red(Alien):
    def __init__(self,canvas):
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()

        super().__init__(canvas, 4, "red", width, height, 2)

    def activate(self, x=None, y=None):
        if x == None and y == None:
            self.x = random.randint(0, self.canvas.winfo_width())
            self.y = 0

            self.x1 = self.x - self.w/2
            self.x2 = self.x + self.w/2
            self.y1 = self.y - self.h/2
            self.y2 = self.y + self.h/2

            self._active = True

            self.alien = self.canvas.create_image(self.x, self.y, anchor=CENTER, image=self.image)



class Alien_green(Alien_red):
    def __init__(self,canvas):
        self.image=PhotoImage(file="alien_green.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()

        Alien.__init__(self, canvas, 4, "green", width, height, 4)
    
    def next(self):
        if self._active == True:
            

            self.wiggle = random.randint(-5,5)

            self.x1 += self.wiggle
            self.x2 += self.wiggle
            self.y1 += self.increment
            self.y2 += self.increment

            self.x += self.wiggle
            self.y += self.increment

            self.canvas.move(self.alien, self.wiggle, self.increment)

            if self.y > self.canvas.winfo_height():
                self.deactivate()
                


class Alien_blue(Alien_red):
    def __init__(self,canvas):
        self.angle = random.randint(-160,-20)

        self.image=PhotoImage(file="alien_blue.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()

        Alien.__init__(self, canvas, 4, "blue", width, height, 3)
    
    def next(self):
        if self._active == True:
            if self.x1 < 0 or self.x2 > self.canvas.winfo_width():
                self.angle = -180 - self.angle

            if self.angle > -90:
                angle_rad = (359-self.angle) *math.pi/180
                
                self.movex = self.increment * math.cos(angle_rad)
                self.movey = self.increment * math.sin(angle_rad) 
            else:
                angle_rad = (self.angle-180) * math.pi/180

                self.movex = -self.increment * math.cos(angle_rad)
                self.movey = self.increment * math.sin(angle_rad) 

            #hitbox movement
            self.x1 += self.movex
            self.x2 += self.movex
            self.y1 += self.movey
            self.y2 += self.movey
            
            #alien center movement
            self.x += self.movex
            self.y += self.movey

            #image movement
            self.canvas.move(self.alien, self.movex, self.movey)

            if self.y > self.canvas.winfo_height():
                self.deactivate()
        
class Alien_mine(Alien_red):
    def __init__(self,canvas):
        self.angle = random.randint(-160,-20)

        self.image=PhotoImage(file="BIDEN WITH NO BRIM.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()

        Alien.__init__(self, canvas, 4, "yellow", width, height, 5)

    def next(self):
        if self._active == True:
            if self.x < 0:
                self.canvas.move(self.alien, self.canvas.winfo_width()-5,0)
                self.x += self.canvas.winfo_width()-5
                self.x1 += self.canvas.winfo_width()-5
                self.x2 += self.canvas.winfo_width()-5
            elif self.x > self.canvas.winfo_width():
                self.canvas.move(self.alien, -self.canvas.winfo_width()+5,0)
                self.x -= self.canvas.winfo_width()-5
                self.x1 -= self.canvas.winfo_width()-5
                self.x2 -= self.canvas.winfo_width()-5


            if self.angle > -90:
                angle_rad = (359-self.angle) *math.pi/180
                
                self.movex = self.increment * math.cos(angle_rad)
                self.movey = self.increment * math.sin(angle_rad) 
            else:
                angle_rad = (self.angle-180) * math.pi/180

                self.movex = -self.increment * math.cos(angle_rad)
                self.movey = self.increment * math.sin(angle_rad) 

            #hitbox movement
            self.x1 += self.movex
            self.x2 += self.movex
            self.y1 += self.movey
            self.y2 += self.movey
            
            #alien center movement
            self.x += self.movex
            self.y += self.movey

            #image movement
            self.canvas.move(self.alien, self.movex, self.movey)

            if self.y > self.canvas.winfo_height():
                self.deactivate()






###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
        alien.deactivate()
    else:
        result="miss!"
    print(x,y,result)
   
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)
        alien=Alien_mine(canvas)

        alien.activate()
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate()
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

