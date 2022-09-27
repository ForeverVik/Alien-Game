from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True
    
def shoot(canvas, aliens, booms, ammo, x, y):
    hit = False
    for alien in aliens:
        if alien.is_active() and alien.is_shot(x,y):
            ammo.increment(alien.value)
            alien.deactivate()

            Explosion.add_explosion(canvas, booms, x, y, 30, alien.color)
            hit = True

    if not hit:
        Explosion.add_explosion(canvas, booms, x, y, 30, "white")
        ammo.increment(-3)
        




################
    
def main(): 
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################



        #To complete (time sleep is 0.01s)
        t=0
        while not game_over:
            ammo = amunition.get_value()
            if t%50 == 0:
                Alien.add_alien(canvas,aliens)
            if ammo <= 0:
                canvas.create_text((canvas.winfo_width()*0.5),(canvas.winfo_width()*0.5)-100,text=str("GAME OVER!"),fill="orange",font=("Courier",25))
                stop_game()
            for boom in booms:
                boom.next()
            for alien in aliens:
                alien.next()

            root.update()
            time.sleep(0.01)
            t+=1
        



          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

