import machine, time

pino = machine.Pin(25, machine.Pin.OUT)

while True:
    pino.value(1)
    time.sleep(1)
    pino.value(0)
    time.sleep(1)