#!/usr/bin/env python3

from picamera2 import Picamera2
from sense_hat import SenseHat, InputEvent
from cv2 import resize,split,INTER_AREA
from signal import pause
from time import sleep
from random import randint

def img_to_pixels(rgb_img,dim=(8,8)):
    pixels=list()
    r,g,b=split(resize(rgb_img,dim,interpolation=INTER_AREA))
    for rr,rg,rb in zip(r,g,b):
        for cr,cg,cb in zip(rr,rg,rb):
            pixels.append([cr,cg,cb])
    return pixels

def pushed_up(event):
    """
    Display sensor data
    """
    temperature=int(round(sense.get_temperature(),0))
    humididity=int(round(sense.get_humidity(),0))
    pressure=int(round(sense.get_pressure(),0))
    north=int(round(sense.get_compass(),0))
    sense.show_message(
        text_string=f"t: {temperature}o   h: {humididity}%   p: {pressure}m   N: {north}o",
        scroll_speed=.075
    )

def pushed_down(event):
    """
    Random pixels
    """
    while event.direction == 'down':
        sense.set_pixel(randint(0, 7),
                    randint(0, 7),
                    randint(0, 255),
                    randint(0, 255),
                    randint(0, 255))
        # refresh event
        events=sense.stick.get_events()
        if events:
            # process the latest
            event=events[-1]
        sleep(.05)


def pushed_left(event):
    pass

def pushed_right(event):
    pass

def pushed_middle(event:InputEvent):
    """
    Sensecam implementation
    """
    while event.direction == 'middle':
        rgb=cam.capture_array()
        pixels=img_to_pixels(rgb)
        sense.set_pixels(pixels)
        # refresh event
        events=sense.stick.get_events()
        if events:
            # process the latest
            event=events[-1]

def refresh_led():
    sense.clear()

def main():
    global cam, sense
    # cam
    cam=Picamera2()
    # about the BGR888 format: 24 bits/pixel, each pixel is [R,G,B] (yes, it's very confusing)
    config=cam.create_preview_configuration({'format':'BGR888','size':(64,64)})
    cam.configure(config)
    cam.start()
    # hat
    sense=SenseHat()
    # config hat
    sense.stick.direction_middle=pushed_middle
    sense.stick.direction_up=pushed_up
    sense.stick.direction_down=pushed_down
    sense.stick.direction_left=pushed_left
    sense.stick.direction_right=pushed_right
    sense.stick.direction_any=refresh_led
    refresh_led()
    sense.low_light=False
    # wait for joystick signals
    pause()

if __name__=='__main__':
    main()
