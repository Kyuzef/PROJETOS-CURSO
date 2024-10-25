def setup():
    fullScreen()

x=0
y=0
def draw():
    global x
    global y
    background(0)
    textSize(50)
    text(key,width/2,height/2)
    fill(255,255,0)
    ellipse(x,y,600,600)
    #x=800,y=400
    fill(0)
    ellipse(x-140,y-100,90,90)
    ellipse(x+100,y-100,90,90)
    fill(255)
    rect(x-100,y+150,200,60)
    if key == 'w':
        y-=10
    elif key =='d':
        x+=10
    elif key == 's':
        y+=10
    elif key == 'a':
        x-=10
