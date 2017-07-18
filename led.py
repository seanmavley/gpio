from gpiozero import LED, PWMLED
from time import sleep
from signal import pause

#led = LED(17)
led = PWMLED(17)
#def blink():
#    while True:
#        led.on()
#        sleep(5)
#        led.off()
#        sleep(1)

led.pulse()
pause()
