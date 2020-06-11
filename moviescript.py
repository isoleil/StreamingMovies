import csv

def searchByDirector():  # function to bring results based on director
    director = input('Which director did you want to watch? ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    for row in csv_file:
       # title, year, age, imdb, rotten, netflix, hulu, prime, disney, directors, genres, \
       # country, language, runtime = row
        if director.lower() == row[9].lower():  # indexing starts from 0, director names are in 10th row of csv
            print(row[0])

def searchByMovie(): #function to tell you if movie can be watched on streaming services
    movie = input('Which movie do you want to watch? ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    exists = False
    for row in csv_file:
        if movie.lower() == row[2].lower():
            exists = True
            print('This movie is available on streaming services')
            break
    if not exists:
        print('This movie is not available to stream')

def searchByRTrating(): #function to search movies ratings on IMDb
    movierating = input('What rating does your movie have on IMDb? ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    for row in csv_file:
        title, year, age, imdb, rotten, netflix, hulu, prime, disney, directors, genres, \
        country, language, runtime = row
        if movierating.lower() == row[0].lower():
            print(imdb, 'out of 10 stars')

def searchByRatings(): #function to return movies below a threshold
    movieratings2 = input('What is the minimum IMDb rating you are willing to watch? ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    csv_file_iter = iter(csv_file);
    next(csv_file_iter)
    for row in csv_file_iter:
        title, year, age, imdb, rotten, netflix, hulu, prime, disney, directors, genres, \
        country, language, runtime = row
        if (movieratings2) <= (row[3]):
            print(title, float(row[3]))

def searchByLength(): #function that returns how long a movie is
    movietime = input('How long is your movie? Type the movie name in. ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    for row in csv_file:
         title, year, age, imdb, rotten, netflix, hulu, prime, disney, directors, genres, \
         country, language, runtime = row
         if movietime.lower() == title.lower():
             print(round(int(runtime)/60,2), 'hours')

def searchByPlatform(): #function that returns what platform your movie is on
    movieplatform = input('Where is your movie available? Type the movie name in. ')
    csv_file = csv.reader(open('/Users/isoleilmontalvo/Downloads/StreamingMoviesKaggle.csv', 'r'))
    csv_file_iter = iter(csv_file);
    next(csv_file_iter)
    for row in csv_file:
        title, year, age, imdb, rotten, netflix, hulu, prime, disney, directors, genres, \
        country, language, runtime = row
        ava = 'This movie is available on '
        if movieplatform.lower() == title.lower():
            if float(netflix)==1:
                ava += 'Netflix'
            if float(hulu)==1 and float(netflix)==1:
                ava += ' and Hulu'
            if float(hulu)==1 and float(netflix)!=1:
                ava += 'Hulu'
            if float(prime)==1 and (float(hulu)==1 or float(netflix)==1):
                ava += ' and Prime Video'
            if float(prime)==1 and (float(hulu)!=1 and float(netflix)!=1):
                ava+= 'Prime Video'
            if float(disney)==1 and (float(hulu)==1 or float(netflix)==1 or float(prime)==1):
                ava += ' and Disney+'
            if float(disney)==1 and (float(hulu)!=1 and float(netflix)!=1 and float(prime)!=1):
                ava +='Disney+'

            print(ava)


if __name__ == "__main__":
    searchByPlatform();