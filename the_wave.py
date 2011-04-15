#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pyglet
from engine import *
import random
jump = 1

class Window(pyglet.window.Window):
	def on_draw(self):
		window.clear()
		background.draw()
		pyglet.graphics.draw(len(terrain)/2, pyglet.gl.GL_TRIANGLE_STRIP, ("v2i", tuple(terrain)))
		sprite.draw()
		
def update(dt):
	global jump
	background.x+=background.hspeed
	sprite.x+=sprite.hspeed
	
	if sprite.y<=get_terrain_y(sprite.x):
		sprite.y=ground.y+ground.height
		sprite.vspeed=0
		sprite.y=get_terrain_y(sprite.x+(sprite.width/2))
		jump = 1
	else:
		sprite.vspeed+=sprite.gravity
		sprite.y+=sprite.vspeed
	if(sprite.y-5<=get_terrain_y(sprite.x)):
	
	if(sprite.y-5>get_terrain_y(sprite.x)):
		if(keys[key.LEFT]):
			sprite.hspeed -= 0.2
		if(keys[key.RIGHT]):
			sprite.hspeed += 0.2
		if(keys[key.SPACE] and jump):
			print "jumpppp"
			sprite.vspeed+=1
			sprite.animate()
			jump = 0;
	else:
		sprite.y=get_terrain_y(sprite.x+(sprite.width/2))
		if(keys[key.LEFT]):
			sprite.hspeed=-3
			sprite.animate()
		elif(keys[key.RIGHT]):
			sprite.hspeed=3
			sprite.animate()
		else:
			sprite.hspeed=0
		if(keys[key.SPACE]):
			sprite.vspeed+=13
			sprite.y+=10
			sprite.animate()
def init_terrain():
	terrain=[0,100, 0,0, 100,100]
	for i in range(100, 800+100, 100):
		terrain.extend([i, 0, i+100,random.randint(50, 100)])
	return terrain
	
def get_terrain_y(x):
	x=int(x)
	y1=terrain[4*(x//100)+1]
	y2=terrain[4*(x//100)+5]
	dx=float(x-100*(x//100))
	#~ if(y1>y2):
		#~ return int(y2+float(abs(y2-y1))/(1+(dx/100)))
	#~ else:
		#~ return int(y2-float(abs(y2-y1))/(1+(dx/100)))
	return y1+int(float(y2-y1)*(dx/100))

terrain=init_terrain()
sprite=Sprite(img="snubbe.png", x=100, y=500, width=32, height=32, gravity=-0.2)
background=Sprite(img="background.png", x=0, y=0, width=1600, height=600, hspeed=-2)
ground=Sprite(img="block.png", x=0, y=0, width=64, height=64, hspeed=-2)
music = pyglet.resource.media('snow.ogg')
music.play()

keys=key.KeyStateHandler()
window=Window(width=800, height=600, caption="The Wave")
window.push_handlers(keys)
pyglet.clock.schedule(update)
pyglet.app.run()

