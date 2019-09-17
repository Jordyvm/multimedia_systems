import time
start = time.time()
input_user = 1;
input_movie = 2;
megaArray = []
inputUserRatings = []
inputMovieUsers = []
usersSameMovie = []

file = open("data/ratings.dat", "r")
for line in file:
    parts = line.split("::")
    del parts[-1]
    megaArray.append(parts)

    if int(parts[0]) == input_user: inputUserRatings.append(parts)
    if int(parts[1]) == input_movie: inputMovieUsers.append(parts)

sumScore = 0
sumMult = 0
for x in range(len(inputMovieUsers)):
    mult = 0
    for y in range(len(inputUserRatings)):
        for z in range(len(megaArray)):
            if inputMovieUsers[x][0] == megaArray[z][0]:
                mult += 4 - abs(int(inputUserRatings[y][2]) - int(megaArray[z][2]))
    sumScore += mult * int(inputUserRatings[y][2])
    sumMult += mult
print("Sumscore: " + str(sumScore) + " and Summultiplier: " + str(sumMult))
print("Average weighted predicted result: " + str(sumScore / sumMult))
print("Total elapsed time: " + '%.4f' % (time.time() - start) + "s")

# for mRating in movieRatings:
#     progress += 1
#     if progress % 23 == 0: print("Comparing rating " + str(progress) + " of " + str(len(movieRatings)), end="\r")
#     mult = 0
#     for i in range(users[mRating.user - 1].index, len(ratings)):
#         if ratings[i].user != mRating.user: break
#         for uRating in userRatings:
#             if uRating.movie == ratings[i].movie:
#                 mult += 4 - abs(uRating.score - ratings[i].score)
#     sumScore += mult * mRating.score
#     sumMult += mult
# print("Sumscore: " + str(sumScore) + " and Summultiplier: " + str(sumMult))
# print("Average weighted predicted result: " + str(sumScore / sumMult))
# print("Total elapsed time: " + '%.4f' % (time.time() - start) + "s")




# print(len(megaArray))
# print(len(inputUserRatings))
# print(len(inputMovieRatings))
#
# print(uRating)
# print(megaArray[0][2])
# print(inputUserRatings[0])
# print(inputMovieRatings)

# for line in megaArray:
#     print(megaArray)
