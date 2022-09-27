from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True
    

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Intialize list of missiles
    missiles=[]
    #Initialize list of Explosions
    booms=[]
    #Initialize list of Aliens
    aliens=[]
    #Initialize counter ammunition
    amunition=Counter(canvas,10)
    amunition.create_text()

    ship=SpaceShip(canvas)
    ship.activate()
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    root.bind("<Up>",lambda e:Missile.add_missile(canvas, missiles, ship.xtracker, ship.y))
    root.bind("<Escape>",lambda e:stop_game())

    t=0
    while True:
        if t%100 == 0:
                Alien.add_alien(canvas,aliens)
        for missile in missiles:
            missile.next()
        for boom in booms:
            boom.next()
        for alien in aliens:
            for missile in missiles:
                if alien.is_active() and alien.is_shot(missile.x, missile.y):
                    alien.deactivate()
                    Explosion.add_explosion(canvas, booms, missile.x, missile.y, 30, alien.color)

            alien.next()
        time.sleep(0.01)     
        root.update() 
        t+=1  # update the graphic (redraw)
    root.mainloop()






if __name__=="__main__":
    main()
