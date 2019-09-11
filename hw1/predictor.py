from data_loader import data, user_ids, movie_ids
from recommender import algo

trainingSet = data.build_full_trainset()

print("Please have patience computing takes a minute.")

algo.fit(trainingSet)

while True:
    print("\n")
    user = int(input("Please enter user: "))
    movie = int(input("Please enter movie: "))
    if user <= len(user_ids) and movie <= len(movie_ids):
        prediction = algo.predict(user,movie)
        result = prediction.est
        print("Prediction for this movie: " + str(result))
    else:
        print("User or movie doesn't exist!")