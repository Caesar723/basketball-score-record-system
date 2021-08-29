import socket
import pygame
import threading
import datetime
import time
running=True
a=datetime.datetime.now()
b=a+datetime.timedelta(minutes = 30)
print(b-a)
red=[input("RedTeamName:"),0,0,0,0,0,0]#分数，犯规，暂停，一分球，两分球，三分球
blue=[input("BlueTeamName:"),0,0,0,0,0,0]
clock=False
ready=True
off=False
offReady=False
offTime=0
over=a-a
thing=['犯规','暂停','一分球','两分球','三分球']
count=True
record=[]
def showMessage(text,size,colour,p,screen,direction):
    fon=pygame.font.Font('/Users/chenxuanpei/opt/anaconda3/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf',size)#把SimHei 路径写入
    sur=fon.render(text,True,colour)
    if direction=='L':
        length=0
        get=fon.metrics(text)
        for i in range(len(get)):
            length=(get[i][1]-get[i][0])+length
        p=[p[0]-length,p[1]]
    if direction=='C':
        length = 0
        get = fon.metrics(text)
        for i in range(len(get)):
            length = (get[i][1] - get[i][0]) + length
        p = [p[0] - (length/2), p[1]]
    screen.blit(sur,p)
def center(screen,p):
    showMessage("VS", 60, ( 0, 0, 0),p, screen,"C")
    showMessage(":", 80, (0, 0, 0), [p[0],p[1]+100], screen, "C")
    showMessage(str(over), 40, (0, 0, 0), [p[0], p[1] + 240], screen, "C")
    showMessage(str(offTime), 50, (0, 0, 0), [p[0], p[1] + 240+100], screen, "C")

def redTeam(screen,p,direct):
    for r in range(len(red)-2):

        size=120if r==1 else 60
        if r==len(red)-3:

            for  i in range(3):
                text = str(red[r+i])
                showMessage(text, size, (255 if r == 0 else 0, 0, 0), [p[0]-80*i, p[1] + (120 if r==2 else 100) * r], screen, direct)
                showMessage(thing[r+i-2], 20, (255 if r == 0 else 0, 0, 0),
                            [p[0] - 80 * i, p[1] + (120 if r == 2 else 100) * r+60], screen, direct)
        else:
            text = str(red[r])
            showMessage(text,size,(255 if r==0 else 0,0,0),[p[0],p[1]+ (120 if r==2 else 100)* r],screen,direct)
            if r!=0 and r!=1:
                showMessage(thing[r-2], 30, (255 if r == 0 else 0, 0, 0), [p[0]-80, p[1]+20 + (120 if r == 2 else 100) * r], screen,
                            direct)



def blueTeam(screen,p,direct):
    for r in range(len(blue) - 2):
        #showMessage(str(blue[r]), 120if r==1 else 60, (0, 0, 255 if r==0 else 0), [p[0], p[1] +  (120 if r==2 else 100)* r], screen,direct)
        size = 120 if r == 1 else 60
        if r == len(blue) - 3:

            for i in range(3):
                text = str(blue[r + i])
                showMessage(text, size, ( 0, 0, 255 if r == 0 else 0), [p[0] + 80 * i, p[1] + (120 if r == 2 else 100) * r],
                            screen, direct)
                showMessage(thing[r + i - 2], 20, (255 if r == 0 else 0, 0, 0),
                            [p[0] + 80 * i, p[1] + (120 if r == 2 else 100) * r + 60], screen, direct)
        else:
            text = str(blue[r])
            showMessage(text, size, ( 0, 0,255 if r == 0 else 0), [p[0], p[1] + (120 if r == 2 else 100) * r], screen,
                        direct)
            if r!=0 and r!=1:
                showMessage(thing[r-2], 30, (255 if r == 0 else 0, 0, 0), [p[0]+80, p[1]+20 + (120 if r == 2 else 100) * r], screen,
                            direct)
def addscore():
    global clock,off
    print("run")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 8888))#8888是端口，客户端要一样
    server.listen(10)
    while running:

        c, a = server.accept()
        get = c.recv(1024).decode()
        print(get, a)
        if get=='R1':
            red[1]=red[1]+1
            red[4]=red[4]+1
        if get=='R2':
            red[1]=red[1]+2
            red[5] = red[5] + 1
        if get=='R3':
            red[1]=red[1]+3
            red[6] = red[6] + 1
        if get=='B1':
            blue[1]=blue[1]+1
            blue[4] = blue[4] + 1
        if get=='B2':
            blue[1]=blue[1]+2
            blue[5] = blue[5] + 1
        if get=='B3':
            blue[1]=blue[1]+3
            blue[6] = blue[6] + 1
        if get=='Rf':
            clock=False
            red[2]=red[2]+1
        if get=='Rp':
            red[3]=red[3]+1
            off=True
        if get=='Bf':
            clock=False
            blue[2]=blue[2]+1
        if get=='Bp':
            blue[3]=blue[3]+1
            off=True
        if get =='start':
            clock=True
        if get=='relax':
            clock=False
        if get=='back' and len(record)!=0:
            if record[len(record)-1]== 'R1':
                red[1] = red[1] - 1
                red[4] = red[4] - 1
            if record[len(record)-1] == 'R2':
                red[1] = red[1] - 2
                red[5] = red[5] - 1
            if record[len(record)-1] == 'R3':
                red[1] = red[1] - 3
                red[6] = red[6] - 1
            if record[len(record)-1] == 'B1':
                blue[1] = blue[1] - 1
                blue[4] = blue[4] - 1
            if record[len(record)-1] == 'B2':
                blue[1] = blue[1] - 2
                blue[5] = blue[5] - 1
            if record[len(record)-1]== 'B3':
                blue[1] = blue[1] - 3
                blue[6] = blue[6] - 1
            if record[len(record)-1]== 'Rf':

                red[2] = red[2] - 1
            if record[len(record)-1]== 'Rp':
                red[3] = red[3] - 1

            if record[len(record)-1]== 'Bf':

                blue[2] = blue[2] - 1
            if record[len(record)-1]== 'Bp':
                blue[3] = blue[3] - 1
            del record[len(record)-1]
        if get!='' and get!='back' and get!='start' and get!='relex':
            record.append(get)
        print(get, a)
    server.close()
pygame.init()
screen=pygame.display.set_mode([740, 600],pygame.FULLSCREEN)
thread=threading.Thread(target=addscore)
thread.start()

while running:
    if clock==True and ready==True:
        ready=False
        now=datetime.datetime.now()

        ove = now + datetime.timedelta(minutes=30)


    if clock==True and off==False:
        now=datetime.datetime.now()
        over=ove-now
        over=over-datetime.timedelta(microseconds=over.microseconds)
    elif ready==False:
        if count==True:
            count=False
            addTime=time.time()
        else:
            if time.time()-addTime>=1:
                addTime=time.time()
                ove=ove+datetime.timedelta(seconds=1)
    if off ==True and offReady==False and clock==True:
        tiN=time.time()
        print(tiN)
        offReady=True
        clock=False
    if offReady==True:
        offTime=60-int(time.time()-tiN)
        if offTime<=0:
            offTime=0
            offReady=False
            off=False
    screen.fill((255, 255, 255))
    redTeam(screen,[220,80],'L')
    blueTeam(screen, [220+320, 80],'R')
    center(screen,[220+160,90])

    for i in pygame.event.get():
        pass
    pygame.display.flip()

pygame.quit()

