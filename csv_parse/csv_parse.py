import csv

# implement most_successful that returns the number of movies published prior to a given year, with associated earnings.

def most_successful(year):

    with open('movies.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {}
        for rows in reader:
            mydict[rows[0]] = rows[1], rows[2]
        
        for movie in mydict.keys():
            if mydict[movie][0] == year:
                print(movie, mydict[movie][0],  mydict[movie][1])

most_successful("1984")