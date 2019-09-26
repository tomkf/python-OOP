import requests 
import string
import random

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
    final_statement = True

    for item in compare_grid:
        statement = False
        if item in user_gird:
            statement = True
        if statement == False:
            final_statement = False
    
    print(final_statement)

# def interpret_results(user_dict):