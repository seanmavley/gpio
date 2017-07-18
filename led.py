from gpiozero import LED, PWMLED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(2)

#led = PWMLED(17)
#def blink():
#    while True:
#        led.on()
#        sleep(5)
#        led.off()
#        sleep(1)

button.when_pressed = led.blink
button.when_released = led.off

pause()
