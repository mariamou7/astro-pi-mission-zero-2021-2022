from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("My name should be Isaak Newton.", scroll_speed = 0.05)

sense.show_message("Humidity is", scroll_speed = 0.05)

a = sense.get_humidity()
a = round(a) 
sense.show_message(str(a))

B = (0, 0, 255)
O = (255, 255, 255)

Greek_flag = [
B, B, O, B, B, O, O, O,
B, B, O, B, B, B, B, B,
O, O, O, O, O, O, O, O,
B, B, O, B, B, B, B, B,
B, B, O, B, B, O, O, O,
B, B, B, B, B, B, B, B,
O, O, O, O, O, O, O, O,
B, B, B, B, B, B, B, B,
]

sense.set_pixels(Greek_flag)
