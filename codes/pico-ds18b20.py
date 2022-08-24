#importação das bibliotecas para pinos, protocolo, sensor e tempo 
import machine, oneWire, ds18x20, time

pinoTemp = machine.Pin(6) #define o pino utilizado na montagem (GPIO6 - pino 9)
sensTemp = ds18x20.DS18X20(oneWire.OneWire(pinoTemp)) #define protocolo
idTemp = sensTemp.scan() #identifica endereço dos sensores conectados
print("Sensores encontrados:",idTemp)

while True:
    sensTemp.convert_temp() #realiza conversão de temperatura (min 750ms)
    time.sleep_ms(750)
    for i in idTemp:
        print(sensTemp.read_temp(i), "oC") #realiza leitura de cada sensor
        time.sleep(1)
