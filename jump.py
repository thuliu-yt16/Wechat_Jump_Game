import numpy as np
from PIL import Image
import math
import time
import os,random



totcnt=0
delta=95


center_x=400
center_y=1200

offset=50



repeattimes=0
im=Image.open('./picture/0.png')
lastpix=im.load()

def printscreen():
    os.system('adb shell screencap -p /sdcard/'+str(totcnt)+'.png')
    os.system('adb pull /sdcard/'+str(totcnt)+'.png ./picture')



def distance():

    printscreen()
    global totcnt,lastpix,repeattimes
    im=Image.open('./picture/'+str(totcnt)+'.png')
    w,h=im.size
    pix=im.load()



    '''
    for i in xrange(w-1,0,-1):
        for j in xrange(h):
            if pix[i,j]!=lastpix[i,j] and repeattimes<2:
                lastpix=pix
                repeattimes+=1
                return 0
    repeattimes=0
    '''
    bodyPos=[]

    for i in xrange(500,800):
        for j in xrange(h):
            r,g,b,a=pix[i,j]
            if abs(r-55)+abs(g-56)+abs(b-97)==0:
                bodyPos.append((i,j))
    body_x=sum([pos[0] for pos in bodyPos])/len(bodyPos)
    body_y=sum([pos[1] for pos in bodyPos])/len(bodyPos)


    pix[body_x,body_y]=255,255,255,255
    is_found=False
    tgt_x=tgt_y=0

    for x in xrange(1200,800,-1):
        if is_found:
            break
        averColor=(pix[x,0][0],pix[x,0][1],pix[x,0][2])
        for y in xrange(h):
            r,g,b,a=pix[x,y]
            if abs(r-averColor[0])+abs(g-averColor[1])+abs(b-averColor[2])>20:
                if abs(y-body_y)<50:
                    continue
                tgt_x=x
                tgt_y=y
                is_found=True
                break


    def findMost(from_x,from_y,dy):
        r,g,b,a=pix[from_x,from_y]
        while 1:
            r1,g1,b1,a=pix[from_x,from_y+dy]
            if abs(r1-r)+abs(g1-g)+abs(b1-b)<5:
                from_y+=dy
                continue
            r1,g1,b1,a=pix[from_x-1,from_y]
            if abs(r1-r)+abs(g1-g)+abs(b1-b)<5:
                from_x-=1
                continue

            return (from_x,from_y)

    (left_x,left_y)=findMost(tgt_x,tgt_y,-1)
    (right_x,right_y)=findMost(tgt_x,tgt_y,1)


    r,g,b,a=pix[tgt_x,tgt_y]
    if abs(r-129)+abs(g-116)+abs(b-224)<5:
        tgt_x-=delta
    elif abs(r-212)+abs(g-176)+abs(b-143)<5:
        tgt_x-=75
    elif abs(min(left_x,right_x)-tgt_x)>25:
        tgt_x=min(left_x,right_x)+5
        if abs(left_x-right_x)<5:
            tgt_y=(left_y+right_y)/2
    else:
        tgt_x-=delta

    '''
    for i in xrange(w):
        pix[i,tgt_y]=0,0,0,255
    for i in xrange(h):
        pix[tgt_x,i]=0,0,0,255
    '''
    return ((tgt_x-body_x)**2+(tgt_y-body_y)**2)**0.5

def jump():
    dis=distance()
    x=random.uniform(0,800)
    y=random.uniform(0,1600)


    swipetime=int(dis*1.64)
    cmd='adb shell input swipe %d %d %d %d %d'%(x,y,x,y,swipetime)

    os.system(cmd)
    time.sleep(1+random.random())
    # time.sleep(0.3+dis*0.001)
    global totcnt
    totcnt+=1


for i in xrange(0,1000):
    jump()
    if i%70==0 and i>0 and delta>50:
        delta*=0.8
#distance()
