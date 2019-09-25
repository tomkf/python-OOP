import csv

# returns most successful movie (in earnings) of given year provided

def takeSecond(elem):
    return int(elem[2])

def most_successful(year):

    with open('movies.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {}
        filtered_list = []

        for rows in reader:
            mydict[rows[0]] = rows[1], rows[2]
        
        for movie in mydict.keys():
            if mydict[movie][0] == str(year):
                filtered_list.append([movie, mydict[movie][0],  mydict[movie][1]])

        for item in filtered_list:
            filtered_list.sort(key=takeSecond)

        return filtered_list[-1][0], "Earnings: $" + filtered_list[-1][2]

user_input = input("enter a year: ")
print("Most successful film of this year: ")
print(most_successful(user_input))