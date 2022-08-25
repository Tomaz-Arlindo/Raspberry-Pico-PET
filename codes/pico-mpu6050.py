#importação das bibliotecas
import machine, time, mpu6050

#define pinos para i2c
i2c = machine.I2C(0, scl= machine.Pin(21), sda= machine.Pin(20), freq=400000)
mpu6050.mpu6050_init(i2c) #inicia configurações do mpu6050 na porta i2c escolhida

#loop de leitura de dados
while True:
    print("Temperature:\t", mpu6050.mpu6050_get_temp(i2c), "°C") #temperatura
    print("Accelerometer:\t", mpu6050.mpu6050_get_accel(i2c), "g") #aceleração 3 eixos
    print("Gyroscope:\t", mpu6050.mpu6050_get_gyro(i2c), "°/s") #giroscópio 3 eixos
    time.sleep_ms(500)
    
