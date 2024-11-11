from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time
import numpy as np




gameoverposition=1000 # ei variable diye game over lekhar position control hobe. car crash korle etar value 0 hoye jabe ar game over lekha show korbe

slowness=.08
crash=False # For detecting car crashed or not


middleline_y=300 # ei variable diyei road er midlle line gula control hobe. Basically eta middle line er bottom point.

centerx=247 # center of car

#Round object parameters
objx=[] # object gular center x
objy=[600,750,750,900,1050,1050,1200,1200,1500,1650,1650,1800]
objradius=[]


for x in range(12): # randomly object er lane assign kortesi. Apatoto 12 ta object nicchi at a time.
     objx.append(random.choice([247-65,247,247+65]))
     objradius.append(12) #initial radius 12 set kortesi


# Square object paramater
temp=random.choice([247-65,247,247+65])


sqcenterx=temp
sqcentery=975
x1=sqcenterx-15
x2=sqcenterx+15
x3=sqcenterx+15
x4=sqcenterx-15
y1=sqcentery-15
y2=sqcentery-15
y3=sqcentery+15
y4=sqcentery+15


score=0



#for drawing circle objects
def objcirc():
 global objy
 global objx
 global objradius


 i=0
 for x in range(len(objx)):
     cinc(objx[i], objy[i], objradius[i])
     i+=1

#For drawing square object
def objsquare():
 global x1,y1,x2,y2,x3,y3,x4,y4
 mqda(x1,y1,x2,y2,x3,y3,x4,y4)

#square er point gula ke given degree angle e rotate kore dibe
def rotatedeg(degree): # quad er 4 ta point ke given degree angle e rotate kore dibe
 global x1,y1,x2,y2,x3,y3,x4,y4,sqcentery,sqcenterx
 a = math.cos(math.radians(degree))
 b = math.sin(math.radians(degree))


 r = np.array([[a, -b, 0],
               [b, a, 0],
               [0, 0, 1]])
 negtrans = np.array([[1, 0, (-1) * sqcenterx],
                      [0, 1, (-1) * sqcentery],
                      [0, 0, 1]])
 transback = np.array([[1, 0, sqcenterx],
                       [0, 1, sqcentery],
                       [0, 0, 1]])
 temp = np.matmul(transback, r)
 compmat = np.matmul(temp, negtrans)



 v1 = np.array([[x1],
                [y1],
                [1]])
 v2 = np.array([[x2],
                [y2],
                [1]])
 v3 = np.array([[x3],
                [y3],
                [1]])
 v4 = np.array([[x4],
                [y4],
                [1]])



 temp=np.matmul(compmat,v1)
 x1=temp[0][0]
 y1=temp[1][0]




 temp = np.matmul(compmat, v2)
 x2 = temp[0][0]
 y2 = temp[1][0]


 temp = np.matmul(compmat, v3)
 x3 = temp[0][0]
 y3 = temp[1][0]




 temp = np.matmul(compmat, v4)
 x4 = temp[0][0]
 y4 = temp[1][0]

#For Drawing middle lines of the road
def middlelines(y): # y er moddhe middleline_y pass hocche.








 # proti column e middleilne_y er sapekkhe 3 ta line separet line thakbe.
 glColor3f(1, 1, 1)
 mldamedium(215, y, 215, y+200)
 mldamedium(215, y-100, 215, y-300 )
 mldamedium(215, y+300, 215, y+500)








 mldamedium(280, y, 280, y + 200)
 mldamedium(280, y - 100, 280, y - 300)
 mldamedium(280, y + 300, 280, y + 500)

#Drawing point 2
def draw_points(x, y):
 glPointSize(2) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#Drawing point 10
def draw_pointsmedium(x, y):
 glPointSize(10) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#Drawing point 30
def draw_pointsbig(x, y):
 glPointSize(30) #pixel size. by default 1 thake
 glBegin(GL_POINTS)
 glVertex2f(x,y) #jekhane show korbe pixel
 glEnd()

#MLDA (Line) 2
def FindZoneAndCvtTo0(x1,y1,x2,y2): #Algoritm=> diff>0 hole x,y swap. ar x,y er modhe je je  negative tader -1 diye multiply








 res=[] # x1,y1,x2,y2,zone eita return korbe








 dx = x2 - x1
 dy = y2 - y1
 diff=abs(dx)-abs(dy)








 if diff>=0: #No Swap
     if (dx>=0): #dx positive








         #Zone 0
         if dy>=0: #dy positive
             res.append(x1)
             res.append(y1)
             res.append(x2)
             res.append(y2)
             res.append(0)








         # Zone 7
         else: #dy negative
             res.append(x1)
             res.append(y1*(-1))
             res.append(x2)
             res.append(y2*(-1))
             res.append(7)








     else: #dx negative








         # Zone 3
         if dy >= 0:  # dy positive
             res.append(x1*(-1))
             res.append(y1)
             res.append(x2*(-1))
             res.append(y2)
             res.append(3)








         # Zone 4
         else:  # dy negative
             res.append(x1*(-1))
             res.append(y1*(-1))
             res.append(x2*(-1))
             res.append(y2*(-1))
             res.append(4)








 else: #diff<0 #Swap lagbe








     if (dx >= 0):  # dx positive








         # Zone 1
         if dy >= 0:  # dy positive
             res.append(y1)
             res.append(x1)
             res.append(y2)
             res.append(x2)
             res.append(1)








         # Zone 6
         else:  # dy negative
             res.append(y1*(-1))
             res.append(x1)
             res.append(y2*(-1))
             res.append(x2)
             res.append(6)








     else:  # dx negative
         # Zone 2
         if dy >= 0:  # dy positive
             res.append(y1)
             res.append(x1*(-1))
             res.append(y2)
             res.append(x2*(-1))
             res.append(2)








         # Zone 5
         else:  # dy negative
             res.append(y1*(-1))
             res.append(x1*(-1))
             res.append(y2*(-1))
             res.append(x2*(-1))
             res.append(5)








 return res
def Cvt0ToX(x,y,zone):
 res=[]
 if(zone==0):
     res.append(x)
     res.append(y)
 elif zone==1:
     res.append(y)
     res.append(x)








 elif zone==2:
     res.append(y*(-1))
     res.append(x)
 elif zone==3:
     res.append(x*(-1))
     res.append(y)
 elif zone==4:
     res.append(x*(-1))
     res.append(y*(-1))
 elif zone==5:
     res.append(y*(-1))
     res.append(x*(-1))
 elif zone==6:
     res.append(y)
     res.append(x*(-1))
 else: # zone==7:
     res.append(x)
     res.append(y*(-1))
















 return res
def mlda(x1,y1,x2,y2):








 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)








 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]








 #Applying Mlda
 dx=x2-x1
 dy=y2-y1








 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx








 d=dint
 x=x1
 y=y1
 while(x<x2):








     #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_points(tp[0],tp[1])








     #Updating pixel








     if(d>0):#choose NE
         x+=1
         y+=1








         d=d+dNE  #updating d
     else: # choose E
         x+=1








         d=d+dE # updating d
#------------------------------------


#MLDA (Line) 10
def mldamedium(x1,y1,x2,y2):








 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)








 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]








 #Applying Mlda
 dx=x2-x1
 dy=y2-y1








 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx








 d=dint
 x=x1
 y=y1
 while(x<x2):








     #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsmedium(tp[0],tp[1])








     #Updating pixel








     if(d>0):#choose NE
         x+=1
         y+=1








         d=d+dNE  #updating d
     else: # choose E
         x+=1








         d=d+dE # updating d
#MLDA (Line) 30
def mldabig(x1,y1,x2,y2):








 #converting to zone 0
 temp=FindZoneAndCvtTo0(x1,y1,x2,y2)








 x1=temp[0]
 y1=temp[1]
 x2=temp[2]
 y2=temp[3]
 prezone=temp[4]








 #Applying Mlda
 dx=x2-x1
 dy=y2-y1








 dE=2*dy
 dNE=2*dy-2*dx
 dint=2*dy-dx








 d=dint
 x=x1
 y=y1
 while(x<x2):








     #Converting the point back to orginal zone and drawing it.
     tp=Cvt0ToX(x,y,prezone)
     draw_pointsbig(tp[0],tp[1])








     #Updating pixel








     if(d>0):#choose NE
         x+=1
         y+=1








         d=d+dNE  #updating d
     else: # choose E
         x+=1








         d=d+dE # updating d

#MCDA (Circle)
def mcda(centerX,centerY,r):
 #print(centerX)
 d=1-r # d initialize

 # initially x =0 ar y =radius
 x=0
 y=r
 while(y>=x): # jotokhon zone 1 e thakbe








     draw_circle_points(x,y,centerX,centerY) #point ta sob zone e draw korbe.








     #Updating pixel








     if(d>=0):#choose SE
















         d=d+2*x-2*y+5
         x += 1
         y -= 1
















     else: # choose E
















         d=d+2*x+3
         x += 1
def draw_circle_points(x,y,centerX,centerY):
 for i in range(8): # i mean zone 0 to 7

     temp=Cvt1ToX(x,y,i) #i th zone er jonno 8 way sym diye point ber kore temp e store kortesi. temp[0]=>x ,temp[1]=>y
     draw_points(temp[0]+centerX,temp[1]+centerY) # point er sathe center jog kore draw kore dicchi.
def Cvt1ToX(x,y,zone):
 res=[]
 if(zone==0):
     res.append(y)
     res.append(x)
 elif zone==1:
     res.append(x)
     res.append(y)








 elif zone==2:
     res.append(x*(-1))
     res.append(y)
 elif zone==3:
     res.append(y*(-1))
     res.append(x)
 elif zone==4:
     res.append(y*(-1))
     res.append(x*(-1))
 elif zone==5:
     res.append(x*(-1))
     res.append(y*(-1))
 elif zone==6:
     res.append(x)
     res.append(y*(-1))
 else: # zone==7:
     res.append(y)
     res.append(x*(-1))
















 return res


#MQDA (Quad)
def mqda(x1,y1,x2,y2,x3,y3,x4,y4):
 mldamedium(x1,y1,x2,y2)
 mldamedium(x2, y2, x3, y3)
 mldamedium(x3, y3, x4, y4)
 mldamedium(x4, y4, x1, y1)

#MQDA filled (filled Quad)
def mqdafilled(x1,y1,x2,y2,x3,y3,x4,y4):
 # mlda(x1,y1,x2,y2)
 # mlda(x2, y2, x3, y3)
 # mlda(x3, y3, x4, y4)
 # mlda(x4, y4, x1, y1)


 for x in range(x1,x2+1,25): #optimize er jonno skip kortesi.
     mldabig(x,y1,x,y4)
 # for y in range(y1,y4+1):
 #     mlda(x1,y,x2,y)

#MQDA filled (filled Quad)
def mqdafilledSmall(x1,y1,x2,y2,x3,y3,x4,y4):
 # mlda(x1,y1,x2,y2)
 # mlda(x2, y2, x3, y3)
 # mlda(x3, y3, x4, y4)
 # mlda(x4, y4, x1, y1)

 for x in range(x1,x2+1): #optimize er jonno skip kortesi.
     mlda(x,y1,x,y4)

 # for y in range(y1,y4+1): #eta use korle slow hoye jay. so alternatively drawpoint er size baraye diyechi.
 #     mlda(x1,y,x2,y)

#Drawing any number between 0 to 9
def drawnum(x,y,num,width, height):#x,y holo midpoint er position ar num holo je number draw korbo. height ar width mid point theke up ar left er distance


 if num=='0':
     mlda(x-width,y-height,x-width,y+height)  #left vertical line
     mlda(x + width, y - height, x + width, y + height)  # right  vertical line
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
 elif num=='1':
     mlda(x + width, y - height, x + width, y + height)
 elif num=='2':
     mlda(x + width, y , x + width, y + height)  # right  vertical line upper half
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
     mlda(x - width, y - height, x - width, y )  # left vertical line lower half
     mlda(x - width, y , x + width, y )  # mid line








 elif num=='3':
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x + width, y - height, x + width, y + height)  # right  vertical line
 elif num=='4':
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x + width, y - height, x + width, y + height)  # right  vertical line
     mlda(x - width, y + height, x - width, y)  # left vertical line upper half
 elif num=='5':
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x - width, y + height, x - width, y)  # left vertical line upper half
     mlda(x + width, y, x + width, y - height)  # right  vertical line lower half
 elif num=='6':
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x - width, y - height, x - width, y + height)  # left vertical line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
     mlda(x + width, y, x + width, y - height)  # right  vertical line lower half
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line








 elif num=='7':
     mlda(x - width, y - height, x + width, y + height)  # cross line
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
 elif num=='8':
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x + width, y - height, x + width, y + height)  # right  vertical line
     mlda(x - width, y - height, x - width, y + height)  # left vertical line
 elif num=='9':
     mlda(x - width, y, x + width, y)  # mid line
     mlda(x + width, y - height, x + width, y + height)  # right  vertical line
     mlda(x - width, y + height, x - width, y)  # left vertical line upper half
     mlda(x - width, y + height, x + width, y + height)  # upper horizontal line
     mlda(x - width, y - height, x + width, y - height)  # lower horizontal line

#8 circles inside a circle
def cinc(x,y,r):
     centerX = x
     centerY = y
     radius = r


     mcda(centerX, centerY, radius)  # big circle

     mcda(centerX + radius / 2, centerY, radius / 2)  # Horizontal right
     mcda(centerX - radius / 2, centerY, radius / 2)  # Horizontal left
     mcda(centerX, centerY + radius / 2, radius / 2)  # vertical up
     mcda(centerX, centerY - radius / 2, radius / 2)  # vertical down


     crossX = (math.sin(math.radians(45))) * radius / 2
     crossY = crossX


     mcda(centerX + crossX, centerY + crossY, radius / 2)  # Cross NE
     mcda(centerX - crossX, centerY + crossY, radius / 2)  # Cross NW
     mcda(centerX + crossX, centerY - crossY, radius / 2)  # Cross SE
     mcda(centerX - crossX, centerY - crossY, radius / 2)  # Cross SW


#For drawing car
def car(centerx):
 glColor3f(0.9, 0.49, 0.494)
 mqdafilledSmall(centerx-17,30,centerx+17,30,centerx+17,100,centerx-17,100)
 glColor3f(0, 0, 0)
 mqdafilledSmall(centerx - 10, 50, centerx + 10, 50, centerx + 10, 80, centerx - 10, 80)

def scoredisplay(b=0):# b is the score
    glColor3f(.1, .1,.8)


    #S

    x, y = 10, 100+350
    for i in range(5):
        mlda(x, y, x+25, y)
        mlda(x+25, y, x + 25, y + 12)
        mlda(x + 25, y + 12, x , y+12)
        mlda(x , y+12, x, y+25)
        mlda(x,y+25,x+25,y+25)
        x += 1
        y += 1
    #C
    x, y = 50, 100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x + 25, y, x, y)
        x += 1
        y += 1
    #O
    x, y = 90, 100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x + 25, y + 25, x + 25, y)
        mlda(x + 25, y, x, y)
        x += 1
        y += 1
    #R
    x, y = 130,100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x + 25, y + 25, x + 25, y + 12)
        mlda(x, y + 12, x + 25, y + 12)
        mlda(x, y + 25, x + 25, y + 25)
        mlda(x, y + 12, x + 25, y)
        x += 1
        y += 1
    #E
    x, y = 170,100+350
    for i in range(5):
        mlda(x, y, x, y + 25)
        mlda(x, y, x + 25, y)
        mlda(x, y + 12, x + 25, y + 12)
        mlda(x, y + 25, x + 25, y + 25)
        x += 1
        y += 1

    x,y=210,120+350
    for i in range(5):
        mlda(x,y+i,x+5,y+i)
        mlda(x,y+i-10,x+5,y+i-10)

    x,y=250,115+350
    for i in str(b):
        drawnum(x,y,i,10,10)
        x+=30

def game_over():
    glColor3f(.5, .5, 1)

    global gameoverposition

    #G
    x,y=10-gameoverposition,350-gameoverposition-50
    for i in range(5):

        mlda(x,y,x+100,y)
        mlda(x,y,x,y+100)
        mlda(x,y+100,x+100,y+100)
        mlda(x+100,y,x+100,y+50)
        mlda(x+100,y+50,x+50,y+50)
        x+=1
        y+=1
    #A
    x,y=135-gameoverposition,350-gameoverposition-50
    for i in range(5):
        mlda(x,y,x+50,y+100)
        mlda(x+50,y+100,x+100,y)
        mlda(x+25,y+50,x+75,y+50)
        x += 1
        y += 1
    #M
    x,y=260-gameoverposition,350-gameoverposition-50
    for i in range(5):
        mlda(x,y,x+25,y+100)
        mlda(x+25,y+100,x+50,y+50)
        mlda(x+50,y+50,x+75,y+100)
        mlda(x+75,y+100,x+100,y)
        x += 1
        y += 1
    #E
    x,y=375-gameoverposition,350-gameoverposition-50
    for i in range(5):
        mlda(x,y,x,y+100)
        mlda(x,y,x+100,y)
        mlda(x,y+50,x+100,y+50)
        mlda(x,y+100,x+100,y+100)
        x += 1
        y += 1
    #O
    x,y=10-gameoverposition,225-gameoverposition-50
    for i in range(5):
        mlda(x,y,x,y+100)
        mlda(x, y+100, x+100, y+100)
        mlda(x+100, y+100, x+100, y)
        mlda(x+100, y, x, y)
        x += 1
        y += 1

    #V
    x,y=135-gameoverposition,225-gameoverposition-50
    for i in range(5):
        mlda(x,y+100,x+50,y)
        mlda(x+50, y, x+100, y+100)
        x += 1
        y += 1


    #E
    x, y = 260-gameoverposition, 225-gameoverposition-50
    for i in range(5):
        mlda(x, y, x, y + 100)
        mlda(x, y, x + 100, y)
        mlda(x, y + 50, x + 100, y + 50)
        mlda(x, y + 100, x + 100, y + 100)
        x += 1
        y += 1
    #R
    x, y = 375-gameoverposition, 225-gameoverposition-50
    for i in range(5):
        mlda(x, y, x, y + 100)
        mlda(x+100, y+100, x + 100, y+50)
        mlda(x, y + 50, x + 100, y + 50)
        mlda(x, y + 100, x + 100, y + 100)
        mlda(x,y+50,x+100,y)
        x += 1
        y += 1


def idle():
  global crash
  if crash==False: # jokhon car crash korbe na sudhu tokhon ei changes gula hobe.
     #difficulty Managing
     global slowness
     time.sleep(slowness) # slowness er value aste aste kombe . so frame rate barbe and game difficult hobe.
     #print(slowness)
     if slowness>0.0002:
         slowness -= .0001


     #Middle line of road update
     global middleline_y
     if middleline_y >0 :  # second line jokhon bottom touch korbe tokhon animation restart hobe. ar line gula amon vabe banano je mone hobe je sudhu niche jacche.
         middleline_y -= 20


     else:
         middleline_y=300


     #___________________________________________________

     #Round object managing
     global objy
     i=0
     for x in range(len(objy)):
         if objy[i]>0: #amar joto gula obj ache , protita obj er y komacchi 10 kore, ar radius baracche so that object scaling hoy.
             objy[i]-=10
             if 100<objy[i]<=500: # Scaling
                 objradius[i]=objradius[i]+.15
         else:# Jokhon object screen er bottom e chole ashbe
             objy[i] = 1350 # abar upore pathye dicchi ar sob value reset kore dicchi
             objx[i]=random.choice([247-65,247,247+65])
             objradius[i]=12

         i+=1


     #Square object managing
     global x1,x2,x3,x4,y1,y2,y3,y4,sqcentery,sqcenterx


     if sqcentery>0: # jokhonn square bottom e reach kore nai
         y1-=10 #protita y value kombe ar 10 degree kore rotate hobe
         y2-=10
         y3 -= 10
         y4 -= 10
         sqcentery-=10
         rotatedeg(10) # 10 degree kore rotate hobe

     else: # jokhon bottom e reach korbe tokhon sob kichu reset kore initial value hoye jabe
         sqcenterx = random.choice([247 - 65, 247, 247 + 65])
         sqcentery = 1350
         x1 = sqcenterx - 15
         x2 = sqcenterx + 15
         x3 = sqcenterx + 15
         x4 = sqcenterx - 15
         y1 = sqcentery - 15
         y2 = sqcentery - 15
         y3 = sqcentery + 15
         y4 = sqcentery + 15


    #--------------------------------------


    # Car crash handling with round object
     global centerx,gameoverposition


     for i in range(len(objy)):
         if objx[i]==centerx and  0<objy[i]<117: # obj er sathe clash
             gameoverposition=0 # game over lekha ashbe
             crash=True



    # Car hit with square object

     global score

     if sqcenterx == centerx and 0<sqcentery<117:
         score+=50 #bonus score add hobe

         # square object ta initial position e chole jabe
         sqcenterx = random.choice([247 - 65, 247, 247 + 65])
         sqcentery = max(objy)- 75 # Alligning in order to avoid object clash
         x1 = sqcenterx - 15
         x2 = sqcenterx + 15
         x3 = sqcenterx + 15
         x4 = sqcenterx - 15
         y1 = sqcentery - 15
         y2 = sqcentery - 15
         y3 = sqcentery + 15
         y4 = sqcentery + 15

     score+=1 #proti frame por por score 1 kore barbe


  else: # car crash korle game over lekha ashbe and screen e kono change hobe na.
      gameoverposition=0

  glutPostRedisplay()
def buttons(key,x,y):
 global centerx
 if key == b'a' and centerx>185: #button a press korle
     centerx -= 65
 if key == b'd'and centerx<310: # button d press korle
     centerx += 65


 glutPostRedisplay()

#Basic Opengl Functions
def iterate():
 glViewport(0, 0, 500, 500)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
 glMatrixMode (GL_MODELVIEW)
 glLoadIdentity()


def showScreen():
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glLoadIdentity()
     iterate()
     #konokichur color set (RGB)
     #call the draw methods here


     # background (Green)
     glColor3f(0, 1, 0)
     mqdafilled(0,0,140,0,140,500,0,500)
     mqdafilled(360, 0, 500, 0, 500, 500, 360, 500)

     #Road
     glColor3f(.52, .52, .491)
     mqdafilled(150, 0, 350,0, 350, 500, 150, 500)

     #Road Side border
     glColor3f(0.949, 0.949, 0.494)
     mqdafilled(140, 0, 150, 0, 150, 500, 140, 500)
     mqdafilled(350, 0, 360, 0, 360, 500, 350, 500)

     #Road middle lines
     middlelines(middleline_y)




     #car
     global centerx
     glColor3f(0.49, 0.949, 0.994)
     car(centerx)

     objcirc()

     objsquare()

     # showing score
     global score
     scoredisplay(score)

     game_over() #game lekha print hobe but initially screen er baire thakbe



     glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(500, 100)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(idle)
glutKeyboardFunc(buttons)
glutMainLoop()