# rpi-sensecam

Display the RPi camera on the 8x8 LED matrix of the sense-hat. This is a redo of @bennuttall's [astro_cam.py](https://github.com/bennuttall/sense-hat-examples/blob/master/python/astro_cam.py) that uses `picamera2` isntead of the deprecated `picamera` package. You'll need a SenseHat as well as a camera module to use this script, of course.

## Installation and usage

1. Install dependencies:

    ```sh
    sudo apt update
    sudo apt install git python3 python3-numpy python3-opencv sense-hat
    sudo apt install python3-picamera2 --no-install-recommends
    ```

1. Enable the I2C interface:

    ```sh
    sudo raspi-config
    ```

1. Reboot!

1. Clone this repo and run the script:

    ```sh
    cd ~
    git clone https://github.com/cgomesu/rpi-sensecam.git
    cd rpi-sensecam/
    ./sensecam.py
    ```

    > **Note.** If your Sense Hat is stuck on the rainbow LED demo that is loaded by default, try appending `dtoverlay=rpi-sense` to the `/boot/firmware/config.txt` file of your RPi.

1. Use the joystick buttons on the sensehat to control which mode to run. The **sensecam** integration is activated via the `middle` button (press the joystick once). Explore other modes by moving the joystick up, down, etc. `left` turns it off (eco mode?).
