import requests 
import string
import random


def generate_grid():
    """
    generates and returns letters for user to pick from, printed in line to console
    """
    grid = []
    for i in range(12):
        grid.append(random.choice(string.ascii_uppercase))    
    print(*grid)
    return grid


def request_word(user_word, user_gird):
    """
    Makes request to API, then compares user responce to grid, and compares if it is a real word or not
    Returns a "final statement" to be parsed
    """
    URL = "https://wagon-dictionary.herokuapp.com/%s" %(user_word)
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

    user_dic = { 'word': user_word, 'pass': final_statement }
    return user_dic


def interpret_results(action, time_equiv, time):
    """
    Takes the final statment and parses it to user, is also passed the time taken to respond, and an integer equiv. of this for the final score
    """
    print("your word:", action['word'])
    print("Time taken to answer:", time)
    print("Your score:", len(action['word']) - time_equiv + 15)
    print("Message:", action['pass'])
