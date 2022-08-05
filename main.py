## import McGregor manager ##
from code import McGregor


## initialize McGregor manager ##
# PARAMS: debug mode, write to spreadhseets, maximum tests
manager = McGregor(True, True, 10)

## run McGregor manager ##
manager.get_data()
#manager.write_sheet()


## finish the program ##
print('## All done! ##')
