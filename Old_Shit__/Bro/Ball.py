import time
import random

class Ball:
    def __init__(self,win,c,x,y,diameter,speedx,speedy,color,width,height):
        self.win = win
        self.c = c
        self.image = c.create_oval(x,y,diameter,diameter,fill=color,outline=color)
        self.speedx = speedx 
        self.speedy = speedy 
        self.d = diameter
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def move(self):
        try:
            coordinates = self.c.coords(self.image)
            # print(coordinates)
            if coordinates[0] > (self.w - (self.d-self.x)) or coordinates[0] < 0 :
                self.c.move(self.image,-(self.speedx),0)
                self.speedx = self.speedx*(-1)
                self.speedx += random.randint(0,5)
                self.speedy += random.randint(0,5)
            elif coordinates[1] > (self.h - (self.d-self.y)) or coordinates[1] < 0 :
                self.c.move(self.image,0,-(self.speedy))
                self.speedy = self.speedy*(-1)
                self.speedx -= random.randint(0,5)
                self.speedy -= random.randint(0,5)
            self.c.move(self.image,self.speedx,self.speedy)
            self.win.update()
            time.sleep(0.01)
        except Exception as e:
            print(e)
            return