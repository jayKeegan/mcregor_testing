from vidgear.gears import CamGear
import cv2
import os


## obtain YT stream frame ##

def get_frame():

   # McGregor LIVE: 24/7 SpaceX Engine Testing & Development for Starship and Falcon 9 Rockets
   stream = CamGear(
      source="https://www.youtube.com/watch?v=cOmmvhDQ2HM",
      stream_mode=True,
      logging=True
   ).start()

   # obtain single stream frame
   frame = stream.read()

   # save this image in our files
   cv2.imwrite(os.path.join(os.path.dirname(__file__), '../screenshots', 'frame.png'), frame)

   # close the stream
   stream.stop()
   return