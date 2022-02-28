from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("My name should be Nikolas Tesla.", scroll_speed = 0.05)

sense.show_message("Humidity is", scroll_speed = 0.05)

a = sense.get_humidity()
a = round(a) 
sense.show_message(str(a))


N = (90, 60, 80)
D = (0, 0, 0)

hads_up=[
D, N, N, D, D, D, D, D,
D, N, N, D, D, D, D, D,
D, N, N, D, D, D, D, D, 
N, N, N, N, N, N, N, D,
N, N, N, N, N, N, N, D,
N, N, N, N, N, N, N, D,
N, N, N, N, N, N, N, D,
D, D, D, D, D, D, D, D,
]

sense.set_pixels(hads_up)
