#!/bin/python3
import pygame as pg
import math as m
#y is done in specified in a special unit, because I am a retard, so this functions
#converts it back
def global_y(x,by):
	return by-y-50
pg.init()
screen=pg.display.set_mode((800,600))
bg=(255,255,255)
gc=(0,0,0)
pc=(255,0,0)
by=500
x=50
y=0
jmpv=2.5
jmp=0
jpu=False
#y,bricks
rows=[[350,5],[290,3],[230,2]]
for i in range(0,13):
	rows[0].append([False,12+i*60])
	rows[1].append([False,12+i*60])
	rows[2].append([False,12+i*60])

rw=50
move=True
while True:
	for event in pg.event.get():
		if event.type==pg.QUIT: exit()
		if event.type==pg.KEYDOWN and event.key==119: # 119=w
			if not jpu and jmp<10:
				jpu=True
	#done in such manner as to make it doable with a simple math function
	if jpu:
		jmp+=jmpv
		if jmp>50: jpu=False
	elif jmp>0: jmp-=jmpv
	y=180*m.sin(jmp*(3.1415/100))
	if pg.key.get_pressed()[pg.K_d] and x<750: x+=5
	if pg.key.get_pressed()[pg.K_a] and x>0: x-=5
	pg.draw.rect(screen,pc,pg.Rect(x,by-y-50,50,50))
	pg.draw.rect(screen,gc,pg.Rect(0,by,800,600))
	for i in range(len(rows)):
		iy=rows[i][0]
		iv=rows[i][1]
		#i love limits hahahahahahah fuck this si not math
		lim=len(rows[i])-1
		j=2
		#basically, if i dont do that hed be trying to draw nonexisting objects which is no good ;(
		while j<=lim:
			pg.draw.rect(screen,(0,0,0),pg.Rect(rows[i][j][1],iy,rw,rw))
			if move: rows[i][j][1]+=iv
			if global_y(y,by)>iy and global_y(y,by)-50<iy:
				if x>rows[i][j][1]-50 and x<rows[i][j][1]+rw:
					del rows[i][j]
					lim-=1
					#print("nya :3")
			j+=1
					
	pg.display.flip()
	screen.fill(bg)
	#print(jmp)
	pg.time.Clock().tick(60)
