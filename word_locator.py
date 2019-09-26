import requests 
import string
import random
# from timeit import default_timer as timer
# from datetime import timedelta



def generate_grid():
    grid = []
    for i in range(12):
        grid.append(random.choice(string.ascii_uppercase))    
    print(*grid)
    return grid

def request_word(user_word, user_gird):
    URL = "https://wagon-dictionary.herokuapp.com/%s" %(user_word)
    # PARAMS = {'address':location} 
    r = requests.get(url = URL) 
    data = r.json() 

    compare_grid = list(user_word.upper())

    exist_in_list = True
    final_statement = "Try Again"

    for item in compare_grid:
        statement = False
        if item in user_gird:
            statement = True
        if statement == False:
            exist_in_list = False

    if exist_in_list == True and data['found'] == True:
        final_statement = "Well Done!"

#     user_dic = { 'word': user_word,
#     'pass': final_statement,
#     'time': ,
#     'score': len(user_word) - time_val + 10
#     }

#     # print(final_statement)
#     interpret_results(user_dic)
    

#  def interpret_results(user_dict):