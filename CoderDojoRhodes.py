from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

w = (255,255,255)
b = (0,0,255)

sense.show_message("My name should be Ada Lovelace.", scroll_speed=0.06,text_colour=b, back_colour=w)

humid = round(sense.get_humidity())
sense.show_message("Humidity= " + str(humid) + "%",scroll_speed=0.06, text_colour=b, back_colour=w)

greek_flag = [
b, b, w, b, b, b, b, b,
b, b, w, b, b, w, w, w,
w, w, w, w, w, b, b, b,
b, b, w, b, b, w, w, w,
b, b, w, b, b, b, b, b,
w, w, w, w, w, w, w, w,
b, b, b, b, b, b, b, b,
w, w, w, w, w, w, w, w,
]
sense.set_pixels(greek_flag)
sleep(2)
