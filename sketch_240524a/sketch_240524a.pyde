x=0
y=0
z=0
v=0
d=150
b=150
f=0
#может это правда,красивый проект?
def setup():
    global f
    size(600,600)
    f=loadImage("haga.jpg")
def draw():
    global x,y,z,v,d,f
    fill(255)
    textSize(100)
    background(200)
    image(f,0,0,600,600)
    text(x,300,100)
    fill(255,0,0)
    rect(d,b,300,300)
    fill(228,245,7)
    text(y,100,580)
    textSize(50)
    text(u"золото",100,480)
    textSize(100)
    fill(220,7,245)
    textSize(50)
    text(u"жетоны",400,480)
    textSize(100)
    text(z,400,580)
    if v == 1:
        frameRate(0.01)
        background(255,255,0)
        textSize(50)
        frameRate(0.01)
        text(u"Конец!!!",100,300)
        frameRate(1)
def mouseClicked():
    global x,y,z,d,b
    if mouseX > d and mouseX < d+300 and mouseY > b and mouseY < b+300:
        x=x+1
        y=y+3
        z=z+1
        d=random(50,550)
        b=random(50,550)
    if x == 30:
        y=y+200
        z=z+100
    if x == 60:
        y=y+300
        z=z+300
    if x == 100:
        frameRate(0.01)
        background(0,255,12)
        textSize(50)
        text(u"Первая сотня!!!",100,300)
        frameRate(0.01)
        frameRate(1)
    if x == 200:
        frameRate(0.01)
        background(3,29,255)
        textSize(50)
        frameRate(0.01)
        text(u"Вторая сотня!!!",100,300)
        frameRate(1)
    if x == 250:
        y=y+random(25,30)
        z=z+random(50,60)
    if x == 300:
        frameRate(0.01)
        background(255,0,225)
        textSize(50)
        frameRate(0.01)
        text(u"Третья сотня!!!",100,300)
        frameRate(1)
    if x == 400:
        frameRate(0.01)
        background(255,0,0)
        textSize(50)
        frameRate(0.01)
        text(u"Четвёртая сотня!!!",100,300)
        frameRate(1)
    if x == 103 and 203 and 303 and 403:
        frameRate(120)
    if x == 500:
        global v
        v=1
