#!/usr/bin/env python3

from picamera2 import Picamera2
from sense_hat import SenseHat
from cv2 import resize,split,INTER_AREA

def img_to_pixels(rgb_img,dim=(8,8)):
    pixels=list()
    r,g,b=split(resize(rgb_img,dim,interpolation=INTER_AREA))
    for rr,rg,rb in zip(r,g,b):
        for cr,cg,cb in zip(rr,rg,rb):
            pixels.append([cr,cg,cb])
    return pixels

def main():
    #hat
    sense=SenseHat()
    sense.clear()
    sense.low_light=False
    #cam
    cam=Picamera2()
    # about the BGR888 format: 24 bits/pixel, each pixel is [R,G,B] (yes, it's very confusing)
    config=cam.create_preview_configuration({'format':'BGR888','size':(64,64)})
    cam.configure(config)
    cam.start()
    try:
        while True:
            rgb=cam.capture_array()
            pixels=img_to_pixels(rgb)
            sense.set_pixels(pixels)
    except:
        sense.clear()
        sense.low_light=True

if __name__=='__main__':
    main()
