#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

motor_a_speed_pin=19
motor_a_direction_pin=20
motor_b_speed_pin=17
motor_b_direction_pin=18

GPIO.setup(motor_a_speed_pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(motor_a_direction_pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(motor_b_speed_pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(motor_b_direction_pin,GPIO.OUT,initial=GPIO.LOW)

def stopB():
    motor_b_direction_control.ChangeDutyCycle(0)
    motor_b_speed_control.ChangeDutyCycle(0)

def forwardB(speed):
    stopB()
    motor_b_direction_control.ChangeDutyCycle(speed)
    motor_b_speed_control.ChangeDutyCycle(100)

def reverseB(speed):
    stopB()
    motor_b_direction_control.ChangeDutyCycle(speed)
    motor_b_speed_control.ChangeDutyCycle(0)

motor_b_speed_control=GPIO.PWM(motor_b_direction_pin,50)
motor_b_direction_control=GPIO.PWM(motor_b_speed_pin,50)
motor_b_speed_control.start(0)
motor_b_direction_control.start(0)
forwardB(50)
time.sleep(5)
forwardB(10)
time.sleep(5)
reverseB(10)
time.sleep(5)
reverseB(50)
time.sleep(5)
stopB()
