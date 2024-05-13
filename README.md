# rpi-sensecam

Display the RPi camera on the 8x8 LED matrix of the sense-hat.

## installation

1. Install dependencies:

    ```sh
    sudo apt update
    sudo apt install git python3 python3-numpy python3-opencv sense-hat
    sudo apt install python3-picamera2 --no-install-recommends
    ```

1. Enable the I2C interace:

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
