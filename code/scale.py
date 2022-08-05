import cv2
import os


## scale images up ##

def scale_images(amount):

   # loop through each image
   for i in range(amount):

      # open the image
      img = cv2.imread(os.path.join(os.path.dirname(__file__), '../screenshots', f'test-{i}.png'), cv2.IMREAD_UNCHANGED)

      # perform the scaling
      scale_percent = 220
      width = int(img.shape[1] * scale_percent / 100)
      height = int(img.shape[0] * scale_percent / 100)
      dim = (width, height)

      # resize image
      resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

      # save updated image
      cv2.imwrite(os.path.join(os.path.dirname(__file__), '../screenshots', f'test-{i}.png'), resized)