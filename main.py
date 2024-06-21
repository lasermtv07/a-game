#!/bin/python3
import pygame as pg
import math as m
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
r1y=350
r1hb=50
row1=[[False, 100,5],[False, 300,5]]
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
	y=150*m.sin(jmp*(3.1415/100))
	if pg.key.get_pressed()[pg.K_d] and x<750: x+=5
	if pg.key.get_pressed()[pg.K_a] and x>0: x-=5
	pg.draw.rect(screen,pc,pg.Rect(x,by-y-50,50,50))
	pg.draw.rect(screen,gc,pg.Rect(0,by,800,600))
	for i in range(len(row1)):
		pg.draw.rect(screen,(0,0,0),pg.Rect(row1[i][1],r1y,r1hb,r1hb))
		if by-y<r1y+r1hb*2 and by-y>r1y+r1hb:
			if x>row1[i][1]-r1hb and x<row1[i][1]+r1hb:
				del row1[i]
				break
	#print(by-y)
	pg.display.flip()
	screen.fill(bg)
	#print(jmp)
	pg.time.Clock().tick(60)
