from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

w = (225, 225, 225)
b = (0, 0, 0)
g = (0, 255 ,0)
s = (200, 225 , 200)
r =(225, 0 ,0)
w = (255,255,255)
B = (0,0,255)

sense.show_message("My name should be Ada Lovelace.", scroll_speed=0.05,text_colour=B, back_colour=w)
sense.show_message("I love Iraq & Greece.", scroll_speed=0.05,text_colour=B, back_colour=w)

humid = round(sense.get_humidity(),1)
sense.show_message("Humidity is " + str(humid) + "%",scroll_speed=0.05, text_colour=B, back_colour=w)

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
sleep(1)

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
sleep(1)
