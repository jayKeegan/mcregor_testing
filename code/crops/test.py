from PIL import Image


import os


## individual test cropping ##

def crop_tests(amount):

   # obtain the taken frame
   original = Image.open(os.path.join(os.path.dirname(__file__), '../../screenshots', 'cropped.png'))

   # cropping points
   test_height = 23
   test_top = 0
   original_height = original.height
   original_width = original.width

   # loop through each possible test
   for i in range(amount):

      # set cropping coordinates
      left = 0
      top = test_top
      right = original_width
      bottom = test_height

      # add height for the next crop
      test_top += 24
      test_height += 24

      # make the cropping
      image = original.crop((left, top, right, bottom))

      # save it as a new image
      image.save(os.path.join(os.path.dirname(__file__), '../../screenshots', f'test-{i}.png'))