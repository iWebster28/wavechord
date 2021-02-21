## wavechord
MakeUofT2021 Project. OpenCV, Kinect, Raspberry Pi 3B+, PyAudio

## Setup

## Hardware
* Raspberry Pi 3 B+
* Kinect (V1)

## Software
* Raspbian Stretch
* OpenCV 3.4.3 (compiled on Raspi)
* Python 3.5.3
* PyAudio
* fswebcam

## To run:
* Compile OpenCV 3.4.3 with this [guide](https://towardsdatascience.com/installing-opencv-3-4-3-on-raspberry-pi-3-model-b-e9af08a9f1d9)  
* Note: reference [this gist](https://gist.github.com/jbienkowski311/ce12c83672fc7c519ed8586832145eb0) to install all the prequisites for ffmpeg, libgstreamer!!
* Note: make sure you configure [more swap space](https://pimylifeup.com/raspberry-pi-swap-file/), around 1 GB is good for OpenCV.  
* Install fswebcam  
* May have to run [these commands](https://stackoverflow.com/questions/17743479/raspberry-pi-with-kinect) to get Kinect working with fswebcam.  
* Get audio on the Pi working with [this guide](https://jeffskinnerbox.wordpress.com/2012/11/15/getting-audio-out-working-on-the-raspberry-pi/)  
* Optional: install realvnc and use [this command](https://stackoverflow.com/questions/15816/changing-the-resolution-of-a-vnc-session-in-linux/3839759) to connect via SSH to the Pi.  

* Run [finger_count.py](./finger_count.py)  
* Moving your hand left to right over the kinect should generate I, IV, and V chords.
