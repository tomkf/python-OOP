from word_locator import request_word, generate_grid


print("********* Welcome to the longest word-game! *********")
print("Here is your grid:")
generate_grid()
print("*****************************************************")
request_word(input("What is your longest word? \n "))