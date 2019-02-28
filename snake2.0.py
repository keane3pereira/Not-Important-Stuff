import turtle
import time
import random

#----- VARIABLES -----------------------------------------------------------------#
delay = 0.07; score = 0; highscore = 0; cut = 0;
segment = []; level = 1; pause = 0; help_pause = 0
colours = ('grey9','#250500','#002040','#402000','#003020','#300030')
body_colours = ('light blue','light pink','light yellow','azure')

#recover highscore
hs_save = open('hs.txt','r')
highscore = int(hs_save.read())

# ----- SPRITES ----------------------------------------------------#

#level 2 bg
yo = turtle.Turtle()
yo.color('grey9')
yo.shape('square')
yo.shapesize(21,29,1)
yo.penup()
yo.goto(-4,-10)
yo.hideturtle()

#background
win = turtle.Screen()               #creates a main window
win.title('Snake')
win.bgcolor('grey9')
win.setup(width = 640, height = 480)#window size
win.tracer(0)                       #turns off screen updates

#options    
opt = turtle.Turtle()
opt.speed(0)
opt.color('white')
opt.penup()
opt.hideturtle()
opt.goto(-37,-100)
opt.clear()

#help
h = turtle.Turtle()
h.penup()
h.color('white')
h.hideturtle()
h.goto(-26,-100)
h.clear()

#snakehead
head = turtle.Turtle()              #creates a sprite
head.speed(0)
head.shape('square')
head.color('grey')
head.penup()                        #if moves no drawing
head.goto(0,0)
head.direction = 'stop'

#snakefood
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(0,100)
food.direction = 'stop'

#score
pen=turtle.Turtle()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write('Level 1   Score:0   High Score:0',
          align = 'center',font = ('Courier',22,'normal'))

#another label
ooo = turtle.Turtle()
ooo.penup()
ooo.hideturtle()
ooo.goto(0,160)
ooo.color('red')
ooo.clear()

# ----- FUNCTIONS ------------------------------------------------------------#

def go_up():
    if head.direction == 'down': return
    head.direction = 'up'
def go_down():
    if head.direction == 'up': return
    head.direction = 'down'
def go_left():
    if head.direction == 'right': return
    head.direction = 'left'
def go_right():
    if head.direction == 'left': return
    head.direction = 'right'

def move():
    if head.direction == 'up': 
        y = head.ycor()
        head.sety(y + 15)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 15)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 15)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 15)

def options():
    global opt,pause,help_pause
    if pause == 1:
        opt.clear()
        pause = 0
        return
    h.clear()
    opt.write('''
    --- GAME PAUSED ---

       New Game - N

         Help - H 
        
        Exit - Del''',
    align = 'center',font = ('Courier',22,'normal'))
    pause = 1; help_pause = 0

def Help():
    global h,help_pause,pause
    if help_pause == 1:
        h.clear()
        help_pause = 0
        return
    opt.clear()
    h.write('''
                     --- HELP ---

    
    yellow food --> 10 pts
        
    red food    --> 50 pts, 3 sec, #SPECIAL#
        
    blue food   --> 10 pts, can shorten body, #SPECIAL#
    ''',align = 'center',font = ('Courier',15,'normal'))
    help_pause = 1; pause = 0
    
#condition for losing
def lose():
    global segment,delay,score,win,head,level,pen,pause,opt,ooo,yo
    time.sleep(1)
    head.goto(0,0)
    for seg in segment:
        seg.goto(1000,1000)
    segment = []
    head.direction = 'stop'
    head.color('grey')
    delay = 0.07
    score = 0; level = 1
    hs_save = open('hs.txt','w').write(str(highscore))
    win.bgcolor('grey9')
    yo.hideturtle();ooo.clear()
    pen.clear()
    pen.write('Level {}   Score:{}   High Score:{}'.format(level,score,highscore),
              align='center',font=('Courier',22,'normal'))               
    opt.clear()
    pause = 0
    
def exit_game():
    win.bye()
    exit()
     
#----- KEYBOARD BINDINGS ------------------------------------------------------------#

win.listen()

win.onkeypress(go_up,'Up')
win.onkeypress(go_down,'Down')
win.onkeypress(go_left,'Left')
win.onkeypress(go_right,'Right')
win.onkeypress(options,'Escape')
win.onkeypress(exit_game,'Delete')
win.onkeypress(lose,'n')
win.onkeypress(Help,'h')

#----- MAIN GAME LOOP ---------------------------------------------------------------#

while True:
    
    win.update()

    if level == 2: #box level, no wrapping around
        if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 190 or head.ycor() < -210:
            lose()

    #check border collision, wrap around
    if head.xcor() > 300:
        head.goto(-300,head.ycor())
    elif head.xcor() < -310:
        head.goto(290,head.ycor())
    elif head.ycor() > 230:
        head.goto(head.xcor(),-220)
    elif head.ycor() < -230:
        head.goto(head.xcor(),220)

    #check body collision
    for i in range(0,len(segment)-1):
        if head.xcor() == segment[i].xcor() and head.ycor() == segment[i].ycor():

            if cut == 1:#special cut food
                for j in range(len(segment)-1,i,-1):
                    segment[j].goto(1000,1000)
                    segment.remove(segment[j])
                head.color('grey');cut = 0;
                food.color('yellow')
                food.shapesize(1)
            else:
                lose()
            break

    #move food to random spot in window range
    if level == 1:
        x = random.randint(-310,310)
        y = random.randint(-230,190)
    elif level == 2:
        x = random.randint(-280,280)
        y = random.randint(-210,170)

        
    #check collision with food

    if head.distance(food) < 20:
        cut = 0; ooo.clear()
        head.color('grey')
        if food.color() == ('cyan','cyan'):
            head.color('cyan')
            cut = 1;
        elif food.color() == ('red','red'):
            ooo.clear()
            score += 50
            food.color('yellow')
            food.shapesize(1)
            
        #increase the score
        score += 10
        if level == 1:
            win.bgcolor(random.choice(colours))
            
        #special food after certain intervals
        if score%15 == 0:
            if level == 2:
                food.color('cyan');
                food.shapesize(1)
        elif score%8 == 0:
            food.color('red')
            start = time.perf_counter()
            food.shapesize(2)
        else:
            food.color('yellow')
            food.shapesize(1)
        food.goto(x,y)
        
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write('Level {}   Score:{}   High Score:{}'.format(level,score,highscore),align='center',font=('Courier',22,'normal'))
        
        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        if level == 2:
            new_segment.color(random.choice(body_colours))
        else:
            new_segment.color('white')
        new_segment.penup()
        segment.append(new_segment)
        
        #shorten the delay
        delay -= 0.001

    #check time for special food
    if food.color() == ('red','red'):
        if time.perf_counter() - start > 3:
            food.goto(x,y)
            food.color('yellow')
            food.shapesize(1)
        time_left = 3 - int(time.perf_counter() - start)
        ooo.clear()
        ooo.pendown()
        ooo.write(str(time_left),font = ('Courier',30,'bold'))

    #move end segments first
    if pause == 0 and help_pause==0:
        for i in range(len(segment)-1,0,-1):
            x = segment[i-1].xcor()
            y = segment[i-1].ycor()
            segment[i].goto(x,y)

        #move second to where head is
        if len(segment) > 0:
            x = head.xcor()
            y = head.ycor()
            segment[0].goto(x,y)
        if level==2:
            yo.showturtle()
    else:
        yo.hideturtle()
        
    #change level
    if score >= 200:
        if level == 1:
            head.goto(0,0)
            win.bgcolor('#406099')
            for i in range(len(segment)):
                segment[i].color(random.choice(body_colours))
            food.goto(x,y)
            delay = 0.07
            level = 2

    if pause == 0 and help_pause==0: #if unpaused everything
        move()
        
    if cut == 1: #speed up snake
        if delay > 0.032:
            time.sleep(delay - 0.03)
    else:
        time.sleep(delay)

win.mainloop()
