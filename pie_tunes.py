import winsound

def make_pi():###VALUE OF PI 
    q,r,t,k,m,x = 1,0,1,1,3,3
    for i in range(500):#some formula online... seems to work :)
        if 4*q+r-t<m*t:
            yield m
            q,r,t,k,m,x = 10*q,10*(r-m*t),t,k,(10*(3*q+r))//t-10*m,x
        else:
            q,r,t,k,m,x = q*k,(2*q+r)*x,t*x,k+1,(q*(7*k+2)+r*x)//(t*x),x+2
bake_pi = []
def create_tune():
    global bake_pi
    for i in make_pi():
        bake_pi.append(i)
    #print(bake_pi)
    print('You have '+str(len(bake_pi))+' notes')
def play_tune():
    global bake_pi
    for i in range(0,len(bake_pi)):#plays note according to digit value
        if bake_pi[i] == 0:
            a = winsound.Beep(220,500)#A3
        elif bake_pi[i] == 1:
            b = winsound.Beep(247,500)#B3
        elif bake_pi[i] == 2:
            c = winsound.Beep(262,500)#C4
        elif bake_pi[i] == 3:
            d = winsound.Beep(294,500)#D4
        elif bake_pi[i] == 4:
            e = winsound.Beep(330,500)#E4
        elif bake_pi[i] == 5:
            f = winsound.Beep(349,500)#F4
        elif bake_pi[i] == 6:
            g = winsound.Beep(392,500)#G4
        elif bake_pi[i] == 7:
            A = winsound.Beep(440,500)#A4
        elif bake_pi[i] == 8:
            B = winsound.Beep(494,500)#B4
        else:
            C = winsound.Beep(523,500)#C5
create_tune()
play_tune()









