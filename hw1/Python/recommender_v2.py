from classes import *
import sys

inputUser = -1
inputMovie = -1

for arg_index in range(len(sys.argv)):
    if(sys.argv[arg_index] == '-m'): inputMovie = int(sys.argv[arg_index + 1])
    if(sys.argv[arg_index] == '-u'): inputUser = int(sys.argv[arg_index + 1])

if inputMovie == -1: print("No movie_id was supplied, you should do this with the -m tag.")
if inputUser == -1: print("No user_id was supplied, you should do this with the -u tag.")
if inputMovie == -1 or inputUser == -1: quit()

ratings = []
users = []
inputUserRatings = []
inputMovieRatings = []

print("Loading the data...")
file = open("data/ratings.dat", "r")
lastUser = -1
for line in file:
    r = Rating(line.split("::"))
    if lastUser != r.user:
        lastUser = r.user
        users.append(User(lastUser,len(ratings)))
    ratings.append(r)
    if inputUser == r.user: inputUserRatings.append(r)
    if inputMovie == r.movie: inputMovieRatings.append(r)

record = -1
topRating = -1
print("Predicting the score...")
for movieRating in inputMovieRatings:
    score = 0
    for i in range(users[movieRating.user - 1].index,len(ratings)):
        if ratings[i].user != movieRating.user: break
        for userRating in inputUserRatings:
            if ratings[i].movie == userRating.movie:
                score += 4 - abs(userRating.score - ratings[i].score)
    if score > record:
        record = score
        topRating = movieRating

print("User " + str(topRating.user) + " recommends this movie with a score of: " + str(topRating.score))
