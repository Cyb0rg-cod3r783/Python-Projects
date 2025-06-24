# Import the time module.
import time 

# Use "pip install plyer" for installing the plyer module. which will help your code to push notifications to your desktop.
from plyer import notification

# Start an Ifinite Loop, so that your program keep running
while True:
    print("Please sip some water") 
    notification.notify(title = "Please drink some water",
                        message = "you need to drink some water") # You can also enter any other remainder message of your choice here.
    
    time.sleep(60*60) # this will pause the execution of the loop for the current iteration.

