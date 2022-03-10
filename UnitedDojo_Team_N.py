from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

b = (0, 0, 0)
g = (0,250,0)
s = (200,255,200)
r = (255,0,0)
w = (255,255,255)
B = (0,0,255)
y = (255, 204, 0)
c = (102, 153, 255)

sense.show_message("Hello.", scroll_speed=0.06,text_colour=B, back_colour=w)
sense.show_message("My name should be Ada Lovelace.", scroll_speed=0.06,text_colour=B, back_colour=w)

humid = round(sense.get_humidity())
sense.show_message("Humidity= " + str(humid) + "%",scroll_speed=0.06, text_colour=B, back_colour=w)

happy_face = [
g, g, g, g, g, g, g, g,
g, w, w, g, g, w, w, g,
g, w, w, g, g, w, w, g,
g, g, g, g, g, g, g, g,
g, g, g, g, g, g, g, g,
g, w, g, g, g, g, w, g,
g, g, w, w, w, w, g, g,
g, g, g, g, g, g, g, g,
]

sad_dry_face = [
y, y, y, y, y, y, y, y,
y, w, w, y, y, w, w, y,
y, w, w, y, y, w, w, y,
y, y, y, y, y, y, y, y,
y, y, y, y, y, y, y, y,
y, y, w, w, w, w, y, y,
y, w, y, y, y, y, w, y,
y, y, y, y, y, y, y, y,
]

sad_wet_face = [
c, c, c, c, c, c, c, c,
c, w, w, c, c, w, w, c,
c, w, w, c, c, w, w, c,
c, c, c, c, c, c, c, c,
c, c, c, c, c, c, c, c,
c, c, w, w, w, w, c, c,
c, w, c, c, c, c, w, c,
c, c, c, c, c, c, c, c,
]

if humid <= 40:
    sense.set_pixels(sad_dry_face)
elif humid >= 85:
    sense.set_pixels(sad_wet_face)
else:
    sense.set_pixels(happy_face)
sleep(2)

italian_flag = [
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
g, g, g, w, w, r, r, r,
]
sense.set_pixels(italian_flag)
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

heart = [
B, r, r, B, B, r, r, B,
r, r, r, r, r, r, r, r,
r, r, r, r, r, r, r, r,
B, r, r, r, r, r, r, B,
B, r, r, r, r, r, r, B,
B, B, r, r, r, r, B, B,
B, B, B, r, r, B, B, B,
B, B, B, B, B, B, B, B,
]
sense.set_pixels(heart)
sleep(2)
