from picamzero import Camera
from time import sleep

#script for taking photos, not finished

cam = Camera()

cam.start_preview()
cam.capture_sequence(f"Pictures/sequence.jpg", num_images=3, interval=2)
cam.stop_preview()
