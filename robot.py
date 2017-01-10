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

def stop():
    motor_a_direction_control.ChangeDutyCycle(0)
    motor_a_speed_control.ChangeDutyCycle(0)
    motor_b_direction_control.ChangeDutyCycle(0)
    motor_b_speed_control.ChangeDutyCycle(0)

def forward(speed):
    stop()
    motor_a_direction_control.ChangeDutyCycle(0)
    motor_a_speed_control.ChangeDutyCycle(speed)
    motor_b_direction_control.ChangeDutyCycle(0)
    motor_b_speed_control.ChangeDutyCycle(speed)

def reverse(speed):
    stop()
    motor_a_direction_control.ChangeDutyCycle(speed)
    motor_a_speed_control.ChangeDutyCycle(0)
    motor_b_direction_control.ChangeDutyCycle(speed)
    motor_b_speed_control.ChangeDutyCycle(0)

motor_b_speed_control=GPIO.PWM(motor_b_direction_pin,50)
motor_b_direction_control=GPIO.PWM(motor_b_speed_pin,50)
motor_b_speed_control.start(0)
motor_b_direction_control.start(0)

motor_a_speed_control=GPIO.PWM(motor_a_direction_pin,50)
motor_a_direction_control=GPIO.PWM(motor_a_speed_pin,50)
motor_a_speed_control.start(0)
motor_a_direction_control.start(0)
forward(10)
time.sleep(5)
forward(50)
time.sleep(5)
reverse(10)
time.sleep(5)
reverse(50)
time.sleep(5)
reverse(25)
time.sleep(5)
stop()
