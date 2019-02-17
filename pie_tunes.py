import winsound

''' plays music based on pi, using winsound,along with a variation if you want to play your own tune '''

'''VALUE OF PI '''
'''some formula online... seems to work :)'''
def make_pi():   
    q,r,t,k,m,x = 1,0,1,1,3,3
    for i in range(500):
        if 4*q+r-t<m*t:
            yield m
            q,r,t,k,m,x = 10*q,10*(r-m*t),t,k,(10*(3*q+r))//t-10*m,x
        else:
            q,r,t,k,m,x = q*k,(2*q+r)*x,t*x,k+1,(q*(7*k+2)+r*x)//(t*x),x+2
            
'''converts into a list'''       
bake_pi = []
for i in make_pi():
    bake_pi.append(i)
    #print(bake_pi)
    
#sets the frequencies of notes A3 to C4
freqs = {0:220,1:247,2:262,3:294,4:330,5:349,6:392,7:440,8:494,9:523,' ':37}
     '''A3, B3, C3, D3, E3, F3, G3, A4, B4, C4, rest'''

for i in bake_pi:
    winsound.Beep(freqs[i],500)

'''in case you want t make your own tune'''
'''
freqs = {'a':220,'b':247,'c':262,'d':294,'e':330,'f'349,
         'g:392,'A':440,'B':494,'C':523,' ':37}
tune = list(input('enter string of tune'))
print(tune)
default_tune = 'ccggAAg ffeeddc'
if tune = '':
    for i in default_tune:
        winsound.Beep(freqs[i],500)
else:
    for i in tune:
        winsound.Beep(freqs[i],500)
'''





