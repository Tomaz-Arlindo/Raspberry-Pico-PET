import machine
import time
import mpu6050

i2c = machine.I2C(0, scl= machine.Pin(21), sda= machine.Pin(20), freq=400000)
mpu6050.mpu6050_init(i2c)
    
while True:
    #print("Temperature:\t", mpu6050.mpu6050_get_temp(i2c), "°C")
    print("Accelerometer:\t", mpu6050.mpu6050_get_accel(i2c), "g")
    #print("Gyroscope:\t", mpu6050.mpu6050_get_gyro(i2c), "°/s")
    time.sleep_ms(500)
    