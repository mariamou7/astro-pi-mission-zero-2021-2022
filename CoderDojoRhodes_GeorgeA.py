from sense_hat import SenseHat
import time
from random import randint

s = SenseHat()
s.low_light = True

s.set_rotation(270)

  
def cc(dr, dg, db, x, y, r):
  a = []
  for j in range(8):
    for i in range(8):
      dist =(((x-i)**2)+((y-j)**2))//2
      k = []
      temp = int(dr * dist /(r * 91))
      if temp > 255:
        temp = 255
      k.append(temp)
      temp = int(dg * dist /(r * 91))
      if temp > 255:
        temp = 255
      k.append(temp)
      temp = int(db * dist /(r * 91))
      if temp > 255:
        temp = 255
      k.append(temp)
      a.append(k)
  return(a)

def screen_col(col):
  a = []
  for i in range(64):
    a.append(col)
  return(a)

a = []
hu = int(s.get_humidity())
s.set_pixels(screen_col([255, 255, 255]))
time.sleep(0.5)
for n in range(50):
  s.set_pixels(screen_col([int(255-(n*255/50)), int(255-(n*255/50)), int(255-(n*255/50))]))
  time.sleep(0.005)
s.show_message("The humidity is " + str(hu) + "%", scroll_speed=0.02)
for n in range(50):
  s.set_pixels(screen_col([int(n*200/50), int(n*200/50), int(n*255/50)]))
  time.sleep(0.005)

cx, cy = 7, 1
ax, ay = 7, 1
cr, cg, cb = randint(0, 255), randint(0, 255), randint(0, 255)
for n in range(4):
  if ax == 1:
    if ay == 1:
      ax, ay = 1, 7
      ar, ag, ab = 255, 255, 0
    else:
      ax, ay = 7, 7
      ar, ag, ab = 0, 255, 0
  else:
    if ay == 1:
      ax, ay = 1, 1
      ar, ag, ab = 255, 0, 0
    else:
      ax, ay = 7, 1
      ar, ag, ab = 0, 0, 255
  
  for m in range(15):
    s.set_pixels(cc(cr, cg, cb, cx, cy, 0.1))
    time.sleep(0.05)
    cx += (cx-ax)/(-5)
    cy += (cy-ay)/(-5)
    cr += (cr-ar)/(-5)
    cg += (cg-ag)/(-5)
    cb += (cb-ab)/(-5)
ax, ay = 3.5, 3.5
ar, ag, ab = 0, 255, 255
for m in range(20):
  s.set_pixels(cc(cr, cg, cb, cx, cy, 0.1))
  time.sleep(0.05)
  cx += (cx-ax)/(-5)
  cy += (cy-ay)/(-5)
  cr += (cr-ar)/(-5)
  cg += (cg-ag)/(-5)
  cb += (cb-ab)/(-5)
cr = 0.1
for m in range(15):
  s.set_pixels(cc(0, 255, 255, 3.5, 3.5, cr))
  time.sleep(0.05)
  cr = ((cr*10.01)**2)/10.01
  
time.sleep(1)
s.show_message("My name should be Alan Turing.", scroll_speed = 0.04)
