#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
# Initialize the EV3 Brick.
ev3 = EV3Brick()
# Initialize the motors.
left_motor = Motor(Port.B)

right_motor = Motor(Port.C)
# Initialize the drive base.

robot = DriveBase(left_motor, right_motor, 

wheel_diameter=55.5,

axle_track=104)

# Initiaize color sensor
cl = ColorSensor(Port.S4)

# Initiaize distance sensor

distance_sensor = UltrasonicSensor(Port.S2)

# arm motor
arm_motor= Motor(Port.A)

# Put the color sensor into COL-COLOR mode.

gyro=GyroSensor(Port.S3)


def left():
    robot.turn(-90)
    while gyro.angle()>-90:
        wait(2)
        break
def right():
    robot.turn(100)
    while gyro.angle()>-95:
        wait(2)
        break

def grab(grabbed):
    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
        back="yes"
        robot.stop()
        time.sleep(2)
        arm_motor.run_target(400, -65)
        time.sleep(2)
        #x="none"
        x = cl.color()
        grabbed+=1
        robot.straight(-787)
        right()
        robot.straight(-350)
        arm_motor.run_target(400, 60)
        green="no"
        BREAK="yes"
        ts = False
        return ts
        '''
        time.sleep(1)
        ts = TouchSensor(Port.S1).pressed()
        '''
        return grabbed
        return x
        return back
        return green
        return BREAK

grabbed=0
BREAK="no"
time.sleep(1)
ts = TouchSensor(Port.S1).pressed()
back="no"
while ts==True:
    x = cl.color()
    print(x)
    if x == Color.GREEN:
        grabbed=0
        BREAK="no"
        back="no"
        ev3.screen.clear()
        ev3.screen.draw_text(40,50,"GREEN")
        wait(2)
        ev3.speaker.play_file(SoundFile.GREEN)
        robot.straight(160)
        robot.turn(-90)
        robot.straight(100)
        robot.turn(90)
        robot.straight(20)
        green="yes"
        while green=="yes":
            x = cl.color()
            print(x)
            while x==Color.RED:
                x = cl.color()
                robot.drive(50, 0)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-815)
                        right()
                        robot.straight(-350)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                        green="no"
                        BREAK="yes"
                        break

            while x==Color.BLACK:
                if back=="yes":
                    back="no"
                    green="no"
                    break
                robot.straight(-15)
                robot.turn(-3)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-830)
                        right()
                        robot.straight(-350)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                        green="no"
                        BREAK="yes"
                        break

    
    elif x==Color.RED:
        grabbed=0
        BREAK="no"
        back="no"
        ev3.screen.clear()
        ev3.screen.draw_text(40,50,"RED")
        wait(2)
        ev3.speaker.play_file(SoundFile.RED)
        robot.straight(160)
        robot.turn(90)
        robot.straight(100)
        robot.turn(-100)
        robot.straight(20)
        green="yes"
        while green=="yes":
            x = cl.color()
            print(x)
            while x==Color.RED:
                x = cl.color()
                robot.drive(50, 0)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        left()
                        robot.straight(-350)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                        green="no"
                        BREAK="yes"
                        break

            while x==Color.BLACK:
                if back=="yes":
                    back="no"
                    green="no"
                    break
                robot.straight(-15)
                robot.turn(3)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        left()
                        robot.straight(-350)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                        green="no"
                        BREAK="yes"
                        break


    elif x==Color.YELLOW:
        grabbed=0
        BREAK="no"
        back="no"
        ev3.screen.clear()
        ev3.screen.draw_text(40,50,"YELLOW")
        wait(2)
        ev3.speaker.play_file(SoundFile.YELLOW)
        ev3.speaker.beep()
        time.sleep(2)
        robot.turn(-180)
        robot.straight(180)
        robot.turn(90)
        robot.straight(25)
        robot.turn(-115)
        robot.straight(40)
        green="yes"
        while green=="yes":
            x = cl.color()
            print(x)
            while x==Color.RED:
                x = cl.color()
                robot.drive(50, 0)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        left()
                        robot.straight(-370)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                            robot.turn(180)
                        green="no"
                        BREAK="yes"
                        break

            while x==Color.BLACK:
                if back=="yes":
                    back="no"
                    green="no"
                    break
                robot.straight(-15)
                robot.turn(3)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        left()
                        robot.straight(-370)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                            robot.turn(180)
                        green="no"
                        BREAK="yes"
                        break

    elif x==Color.BLUE:
        grabbed=0
        BREAK="no"
        back="no"
        ev3.screen.clear()
        ev3.screen.draw_text(40,50,"BLUE")
        wait(2)
        ev3.speaker.play_file(SoundFile.BLUE)
        ev3.speaker.beep()
        time.sleep(2)
        robot.turn(180)
        robot.straight(180)
        robot.turn(-90)
        robot.straight(40)
        robot.turn(115)
        robot.straight(30)
        green="yes"
        while green=="yes":
            x = cl.color()
            print(x)
            while x==Color.RED:
                x = cl.color()
                robot.drive(50, 0)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        right()
                        robot.straight(-400)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                            robot.turn(180)
                        green="no"
                        BREAK="yes"
                        break

            while x==Color.BLACK:
                if back=="yes":
                    back="no"
                    green="no"
                    break
                robot.straight(-15)
                robot.turn(-3)
                x = cl.color()
                print(x)
                if grabbed==0:
                    if distance_sensor.distance() <50 and distance_sensor.distance() > 40:
                        back="yes"
                        robot.stop()
                        time.sleep(2)
                        arm_motor.run_target(400, -65)
                        time.sleep(2)
                        #x="none"
                        grabbed+=1
                        robot.straight(-787)
                        right()
                        robot.straight(-400)
                        ev3.speaker.play_file(SoundFile.TOUCH)
                        time.sleep(3)
                        ts = TouchSensor(Port.S1).pressed()
                        if ts==True:
                            arm_motor.run_target(400, 60)
                            robot.turn(180)
                        green="no"
                        BREAK="yes"
                        break

    else:
        pass
