
import RPi.GPIO as GPIO
import time

relay_pin = 4 #Change PIN If Needed  (aka phyically pin 7 on pi board.)

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin,GPIO.OUT)


# Every half hour turn relay/valve on for 45 seconds.
try:
        while True:
                #set low
                GPIO.output (relay_pin,GPIO.LOW)
                ts = time.gmtime()
                str = time.strftime("%Y-%m-%d %H:%M:%S", ts)
                print ("Setting low - ON", str)
                time.sleep(45) #Time Is In Seconds (60 for a minute)

                #set high
                GPIO.output (relay_pin, GPIO.HIGH)
                ts = time.gmtime()
                print ("Setting high - OFF",time.strftime("%Y-%m-%d %H:%M:%S", ts))
                time.sleep(1800) #Time Is In Seconds (30mins is 30*60 = 1800)

except KeyboardInterrupt:
        GPIO.cleanup()
        print ("Done")




