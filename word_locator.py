import requests 



def generate_grid():
    print("Q F M R K L I T P")

def request_word(user_word):
    URL = "https://wagon-dictionary.herokuapp.com/%s" %(user_word)
    # PARAMS = {'address':location} 
    r = requests.get(url = URL) 
    data = r.json() 
    print(data)



# request_word("dog")