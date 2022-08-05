import re
from code.filter import check_ending_allowed

## get specifics of each test ##

tests_data = []

def get_final_data(tests):
      
   # loop through each test
   for test in tests:

      # check if no tests so far
      if test.lower().startswith("no tests"):
         tests_data.append(["No tests", "No tests", "No tests"])
      
      else:

         # get the time
         time_regex = r"\d{1,2}:\d{2}:\d{2,3}\s?\w{2}"
         time = re.search(time_regex, test)
         original_time = time.group(0)
         time = re.sub(r'[^a-zA-Z0-9:]', '', original_time).strip()

         # get the stand
         time_index = test.index(original_time)
         stand = test[:time_index].strip()
         stand_temp = re.sub(r'[^a-zA-Z0-9 ]', '', stand).strip()
         stand = check_ending_allowed(stand_temp)
         if stand == None:
            stand = stand_temp

         # get test duration
         duration_index = time_index + len(time)
         duration = test[duration_index:].strip()
         duration = re.sub(r'[^a-zA-Z0-9:]', '', duration).strip()
         # fix common errors
         duration = duration.replace("M", "")
         duration = duration.replace("T", "7")

         # replace possible final "5" confused with "s"
         if duration[-1] == '5':
            duration = duration[:-1] + 's'

         # remove text after "s", "PB" or "SP"
         if duration.startswith("PB"):
            duration = "PB"
         elif duration.startswith("SP"):
            duration = "SP"
         else:
            duration = duration.replace("S", "5")
            splt = duration.split("s")
            duration = splt[0] + "s"

         # check if it was an abort
         if duration.startswith('1s'):
            duration = 'ABORT'

         # save in dictionary
         test_data = {
            0: stand,
            1: time,
            2: duration
         }
         tests_data.append(test_data)

   return tests_data