import socket
import pygame
running=True
#message=input("please")
#door.send(message.encode())
RedType=[input('RedTeam:'),'加一分(one point)','加两分(two point)','加三分(three point)','犯规（foul）','暂停（pause）']
BlueType=[input('BlueTeam:'),'加一分(one point)','加两分(two point)','加三分(three point)','犯规（foul）','暂停（pause）']
centerType=['开始(start)','休息(relax)','撤回(back)']
def showMessage(text,size,colour,p,screen,direction):
    fon=pygame.font.Font('/Users/chenxuanpei/opt/anaconda3/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf',size)
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
pygame.init()
screen=pygame.display.set_mode([740, 480])
def red(screen,p):
    for r in range(len(RedType)):
        showMessage(RedType[r], 20, (255 if r == 0 else 0, 0, 0), [p[0], p[1] + 70 * r], screen,
                    'L')
def blue(screen,p):
    for r in range(len(BlueType)):
        showMessage(BlueType[r], 20, ( 0, 0,255 if r == 0 else 0), [p[0], p[1] + 70 * r], screen,
                    'R')
def center(screen,p):
    showMessage(centerType[0], 25, (0, 0, 0), p, screen, "C")
    showMessage(centerType[1], 25, (0, 0, 0), [p[0],p[1]+100], screen, "C")
    showMessage(centerType[2], 25, (0, 0, 0), [p[0], p[1] + 200], screen, "C")

while running:
    screen.fill((255, 255, 255))
    red(screen,[180,10])
    blue(screen,[500,10])
    center(screen,[370,30])
    for i in pygame.event.get():
        if i.type ==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            hostN = '172.20.10.3'#ip地址要和服务器的一样要连同一个ip
            postNum = 8888
            door = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            door.connect((hostN, postNum))
            if pos[0]>20 and pos[0]<200 :
                if pos[1]>80 and pos[1]<100:
                    door.send('R1'.encode())

                if pos[1] > 150 and pos[1] < 170:
                    door.send('R2'.encode())
                if pos[1] > 220 and pos[1] < 240:
                    door.send('R3'.encode())
                if pos[1] > 290and pos[1] < 310:
                    door.send('Rf'.encode())
                if pos[1] > 290+70and pos[1] < 310+70:
                    door.send('Rp'.encode())
            if pos[0]>500 and pos[0]<680 :
                if pos[1]>80 and pos[1]<100:
                    door.send('B1'.encode())

                if pos[1] > 150 and pos[1] < 170:
                    door.send('B2'.encode())
                if pos[1] > 220 and pos[1] < 240:
                    door.send('B3'.encode())
                if pos[1] > 290and pos[1] < 310:
                    door.send('Bf'.encode())
                if pos[1] > 290+70and pos[1] < 310+70:
                    door.send('Bp'.encode())
            if pos[0]>320 and pos[0]<440 :
                if pos[1] >30and pos[1] < 55:
                    door.send('start'.encode())
                if pos[1] >30+100and pos[1] < 55+100:
                    door.send('relax'.encode())
                if pos[1] >30+200and pos[1] < 55+200:
                    door.send('back'.encode())
            door.close()
    pygame.display.flip()

pygame.quit()



