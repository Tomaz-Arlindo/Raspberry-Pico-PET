import machine, oneWire, ds18x20, time

pinoTemp = machine.Pin(6)
sensTemp = ds18x20.DS18X20(oneWire.OneWire(pinoTemp))
idTemp = sensTemp.scan()
print("Sensores encontrados:",idTemp)

while True:
    sensTemp.convert_temp()
    time.sleep_ms(750)
    for i in idTemp:
        print(sensTemp.read_temp(i), "oC")
        time.sleep(1)
    print("\n")