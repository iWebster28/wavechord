import time 
import os 

while True: # do forever

    # 'fswebcam -r 224x224 --no-banner /home/pi/Desktop/%H%M%S.jpg'
    #'fswebcam -r 224x224 -S 3 --jpeg 50 --save /home/pi/Desktop/%H%M%S.jpg'
    os.system('fswebcam -r 224x224 --no-banner /home/pi/Desktop/%H%M%S.jpg') # uses Fswebcam to take picture
    #"fswebcam -d /dev/video0 -r 640x480 --no-banner " + directory + "1img" + str(num) + ".png"

    time.sleep(1) # this line creates a 15 second delay before repeating the loop