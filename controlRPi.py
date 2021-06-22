import RPi.GPIO as GPIO
import time

#角度轉換為duty cycle
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle

#控制伺服馬達pwm 開啟
def turn_on():
    dc = angle_to_duty_cycle(63)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.2)
    
    dc = angle_to_duty_cycle(91)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)
    
    pwm.ChangeDutyCycle(0)

#控制伺服馬達pwm 關閉
def turn_off():
    dc = angle_to_duty_cycle(112)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.2)
    
    dc = angle_to_duty_cycle(87)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)
    
    pwm.ChangeDutyCycle(0)

#init
MONITOR_PIN = 16
CONTROL_PIN = 12
PWM_FREQ = 50
STEP=15 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
GPIO.setup(MONITOR_PIN, GPIO.IN)

pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)

