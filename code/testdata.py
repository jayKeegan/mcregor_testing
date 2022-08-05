import cv2
import pytesseract
import os
import re


## get data from images ##

# list where data will be saved
tests = []

def get_test_data(debug, amount):

   # loop through each test
   for i in range(amount):

      # open the image
      img = cv2.imread(os.path.join(os.path.dirname(__file__), '../screenshots', f'test-{i}.png'), cv2.IMREAD_GRAYSCALE)

      # blur the background
      bg = cv2.medianBlur(img, 51)

      # get the output
      out = 255 - cv2.absdiff(bg, img)

      # extract text from images
      text = pytesseract.image_to_string(out, lang='eng', config='--psm 12')
      # remove newlines
      text = text.replace("\n", " ")
      # remove special characters
      text = re.sub(r'[^a-zA-Z0-9: ]', '', text).strip()
      # remove many spaces
      text = ' '.join(text.split()).strip()

      # print information if on debug mode
      if debug == True:
         print("OCR: " + text)

      if len(text) < 15:
         pass
      else:
         # append to testing array
         tests.append(text)

   return tests