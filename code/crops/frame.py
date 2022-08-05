from PIL import Image
import os


## image cropping ##

def crop_frame():

   # obtain the taken frame
   original = Image.open(os.path.join(os.path.dirname(__file__), '../../screenshots', 'frame.png'))

   # cropping points
   width, height = original.size
   left = 55
   top = 77
   right = width - 1535
   # TESTING ONLY -> right = width - 1450
   bottom = height - 700

   # make the cropping
   image = original.crop((left, top, right, bottom))

   # save it as a new image
   image.save(os.path.join(os.path.dirname(__file__), '../../screenshots', 'cropped.png'))