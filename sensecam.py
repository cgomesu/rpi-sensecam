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
    sense=SenseHat()
    cam=Picamera2()
    config=cam.create_preview_configuration({'format':'RGB888','size':(640,480)})
    cam.configure(config)
    cam.start()
    while True:
        rgb=cam.capture_array()
        pixels=img_to_pixels(rgb)
        sense.set_pixels(pixels)

if __name__=='__main__':
    main()
