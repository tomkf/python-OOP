
from timeit import default_timer as timer
from datetime import timedelta

from word_locator import request_word, generate_grid, interpret_results

"""
User runs this file with command 'python3 user_interface.py', all interaction with the game done here
Calls module functions and passes them the required parameters. 
"""

print("********* Welcome to the longest word-game! *********")
print("Here is your grid:")
user_grid = generate_grid()
start = timer()
print("*****************************************************")
user_action = request_word(input("What is your longest word? \n "), user_grid)
end = timer()
print("******** Now your results ********")
time_val = timedelta(seconds=end-start)

interpret_results(user_action, int(time_val.seconds), time_val)