import machine
import time
import _thread


internal_led = machine.Pin(25, machine.Pin.OUT)

def second_thread():
    while True:
        print("Hello, I'm here in the second thread writting every second")
        time.sleep(1)

_thread.start_new_thread(second_thread, ())

while True:
    internal_led.toggle()
    time.sleep(0.25)
    