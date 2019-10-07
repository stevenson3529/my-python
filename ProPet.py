from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggleEyes():
    currentColor = c.itemcget(eyeLeft,'fill')
    newColor = c.body_color if currentColor == 'white' else 'white'
    currentState = c.itemcget(pupilLeft,'state')
    newState = NORMAL if currentState == HIDDEN else HIDDEN
    c.itemconfigure(pupilLeft, state = newState)
    c.itemconfigure(pupilRight, state = newState)
    c.itemconfigure(eyeLeft, fill = newColor)
    c.itemconfigure(eyeRight, fill = newColor)
    
def blink():
    toggleEyes()
    root.after(250,toggleEyes)
    root.after(3000,blink)

def togglePupils():
    if not c.eyesCrossed:
        c.move(pupilLeft, 10, -5)
        c.move(pupilRight,-10,-5)
        c.eyesCrossed = True
    else:
        c.move(pupilLeft,-10,5)
        c.move(pupilRight,10,5)
        c.eyesCrossed = False

def toggleTongue():
    if not c.tongueOut:
        c.itemconfigure(tongueTip,state = NORMAL)
        c.itemconfigure(tongueMain,state= NORMAL)
        c.tongueOut = True
    else:
        c.itemconfigure(tongueTip,state = HIDDEN)
        c.itemconfigure(tongueMain, state=HIDDEN)
        c.tongueOut = False

def cheeky(event):
    toggleTongue()
    togglePupils()
    hideHappy(event)
    root.after(1000, toggleTongue)
    root.after(1000, togglePupils)
    return

def showHappy(event):
    if(20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheekLeft, state = NORMAL)
        c.itemconfigure(cheekRight, state = NORMAL)
        c.itemconfigure(mouthHappy, state = NORMAL)
        c.itemconfigure(mouthNormal, state = HIDDEN)
        c.itemconfigure(mouthSad, state = HIDDEN)
        c.happyLevel = 10
    return

def sad():
    if c.happyLevel == 0:
        c.itemconfigure(mouthHappy,state = HIDDEN)
        c.itemconfigure(mouthNormal,state = HIDDEN)
        c.itemconfigure(mouthSad,state = NORMAL)
    else:
        c.happyLevel -= 1
    root.after(500, sad)



#call canvas
root = Tk()

#create canvas
c = Canvas(root, width=400, height=400)
c.configure (bg = '#DBAA2C', highlightthickness = 0)

#draw the pet
c.body_color = '#39A47D'
body = c.create_oval(35,20,365,350, outline = c.body_color,fill=c.body_color)
earLeft = c.create_polygon(75,80,75,10,165,70, outline = c.body_color,fill = c.body_color)
earRight = c.create_polygon(255,45,325,10,320,70,outline=c.body_color,fill=c.body_color)
footLeft = c.create_oval(65,320,145,360,outline=c.body_color,fill = c.body_color)
footRight = c.create_oval(250,320,330,360,outline = c.body_color,fill = c.body_color)
eyeLeft = c.create_oval(130,110,160,170,outline = 'black',fill = 'white')
pupilLeft = c.create_oval(140,145,150,155,outline = 'black',fill = 'black')
eyeRight = c.create_oval(230,110,260,170,outline = 'black',fill = 'white')
pupilRight = c.create_oval(240,145,250,155,outline = 'black',fill = 'black')

#CHANGE MOODS
mouthNormal = c.create_line(170,250,200,272,230,250,smooth = 1, width = 2, state = NORMAL)
mouthHappy = c.create_line(170,250,200,272,230,250,smooth = 1, width = 2, state = HIDDEN)
mouthSad = c.create_line(170,250,200,232,230,250,smooth = 1, width = 2, state = HIDDEN)

#draw tongue
tongueMain = c.create_rectangle(170,250,230,290,outline = 'red',fill = 'red', state = HIDDEN)
TongueTip = c.create_oval(170,285,230,300,outline = 'red',fill = 'red', state = HIDDEN)

#draw mood
cheekLeft = c.create_oval(70,180,120,230,outline = 'pink', fill = 'pink', state = HIDDEN)
cheekLeft = c.create_oval(280,180,330,230,outline = 'pink', fill = 'pink', state = HIDDEN)

c.pack()

#call mood function
c.bind('<Motion>', showHappy)

#call hide function
c.bind('<Leave>', hideHappy)

#call cheeky function
c.bind('<Double-1>',cheeky)

#sets up flags, checks if ProPet's eyes are closed,tongue is out + happiness level
c.happyLevel = 0
c.eyesCrossed = False
c.tongueOut = False

#call blink fn
root.after(1000, blink)

#call sad fn
root.after(5000,sad)

root.mainloop()
