from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

b=(0,0,0)
w=(255,255,255)
sense.show_message("My name should be Ada Lovelace", back_colour=w, text_colour=b, scroll_speed=0.065)

o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
r =(225, 0 ,0)
B = (0,0,255)

humid = round(sense.get_humidity(), 1)
sense.show_message( "Humidity is " + str(humid) + " %",  text_colour=b, back_colour=w, scroll_speed=0.06)

iraq =[
  r, r, r, r, r, r, r, r,
  r, r, r, r, r, r, r, r,
  r, r, r, r, r, r, r, r,
  w, g, g, w, w, g, g, w,
  w, g, g, w, w, g, g, w,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  ]
sense.set_pixels(iraq)
sleep(2)

greek_flag = [
B, B, w, B, B, B, B, B,
B, B, w, B, B, w, w, w,
w, w, w, w, w, B, B, B,
B, B, w, B, B, w, w, w,
B, B, w, B, B, B, B, B,
w, w, w, w, w, w, w, w,
B, B, B, B, B, B, B, B,
w, w, w, w, w, w, w, w,
]
sense.set_pixels(greek_flag)
sleep(2)

wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]

dry = [
  c, c, g, g, c, c, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, g, g, g, g, g, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
]

if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
sleep(2)

