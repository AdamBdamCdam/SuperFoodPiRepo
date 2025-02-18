#from picamzero import Camera
from time import sleep, gmtime, strftime
import schedule

#cam = Camera()
picname = "Pictures/Cress1_{time}.jpg"

def task():
    cam.start_preview()
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    cam.take_photo(picname.format(time = time))
    cam.stop_preview()


# Schedule the task to run every hour
schedule.every(1).hour.do(task)

while True:
    schedule.run_pending()
    sleep(60)  # Check every minute
