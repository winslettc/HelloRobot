import gopigo
import time


class Piggy(object):
    def _init_(selfself):
        print("I AM ALIVE")

    def cha_cha(self):
        """The robot will cha cha/ dance"""
        for x in range(5):
        right_rot()
        time.sleep(.5)
        left_rot()
        time.sleep(.5)
        stop()

    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15) # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(self):
        """Drive forward, constantly scanning, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            tim.sleep(.2)

    def servo_sweep(self):
        """"loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)



p = Piggy()
# p.cha_cha(