## import libraries ##
from code.stream import get_frame
from code.scale import scale_images
from code.testdata import get_test_data
from code.final import get_final_data
from code.gsheets import update_spreadsheet

from code.crops.frame import crop_frame
from code.crops.test import crop_tests


## McGregor manager ##
class McGregor:

   def __init__(self, debug=False, writeToSheet=False, maxTests=10):
      print("### MCGREGOR ENGINE TESTING DETECTOR ###")

      # declare global variables
      self.debug = debug
      self.writeToSheet = writeToSheet
      self.maxTests = maxTests


   @staticmethod
   def print_info(data):

      # print obtained information
      print(data)
      print("\n")


   def get_data(self):

      # get stream's frame
      get_frame()

      # crop the test graph from the stream
      crop_frame()

      # crop individual tests from the cropped graph
      crop_tests(self.maxTests)

      # scale each individual test
      scale_images(self.maxTests)

      # obtain tests information (OCR)
      tests = get_test_data(self.debug, self.maxTests)

      # obtain final data
      tests_data = get_final_data(tests)

      # log them out if on debug mode
      if self.debug == True:
         self.print_info(tests)
         self.print_info(tests_data)

      # declare variable globally
      self.tests_data = tests_data


   def write_sheet(self):

      # check if data should be recorded
      if self.writeToSheet == True:

         # update google sheets information
         update_spreadsheet(self.tests_data)

