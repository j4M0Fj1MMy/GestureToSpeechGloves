import smbus			#import SMBus module of I2C
from time import sleep          #import
import RPi.GPIO as GPIO

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


gpio_array = [6,5,22,27,17]
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
listOfValues = [[],[],[],[],[]]

def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def select_mpu(gpio_pin):
	
	GPIO.output(gpio_array, GPIO.HIGH)

	GPIO.output(gpio_pin, GPIO.LOW)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

count = 0
try:
	while True:
		count = count%len(gpio_array)
		# print(f"doing {gpio_array[count]}")
		select_mpu(gpio_array[count])

		#Read Accelerometer raw value
		acc_x = read_raw_data(ACCEL_XOUT_H)
		acc_y = read_raw_data(ACCEL_YOUT_H)
		acc_z = read_raw_data(ACCEL_ZOUT_H)
	
		#Read Gyroscope raw value
		gyro_x = read_raw_data(GYRO_XOUT_H)
		gyro_y = read_raw_data(GYRO_YOUT_H)
		gyro_z = read_raw_data(GYRO_ZOUT_H)
		
		#Full scale range +/- 250 degree/C as per sensitivity scale factor
		Ax = acc_x/16384.0
		Ay = acc_y/16384.0
		Az = acc_z/16384.0
	
		Gx = gyro_x/131.0
		Gy = gyro_y/131.0
		Gz = gyro_z/131.0
	
		row = f'Gx={round(Gx,2)} Gy={round(Gy,2)} Gz={round(Gz,2)} Ax={round(Ax,2)} Ay={round(Ay,2)} Az={round(Az,2)}'
		# row = ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
		listOfValues[count].append(row)
		# print(row)
		
		# sleep(0.1)
		count+=1
except:
	GPIO.cleanup()
	for i in listOfValues:
		print('')
		for j in i:
			
			print(j)
