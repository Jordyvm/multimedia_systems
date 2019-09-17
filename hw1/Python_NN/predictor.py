from data_loader import data, user_ids, movie_ids
from recommender import algo

# Load the training data
trainingSet = data.build_full_trainset()

print("Please have patience computing takes a minute.")

# Train the NN
algo.fit(trainingSet)

while True:
    print("\n")
    user = int(input("Please enter user: "))
    movie = int(input("Please enter movie: "))
    if user <= len(user_ids) and movie <= len(movie_ids):
        # Predict and display the results
        prediction = algo.predict(user,movie)
        result = prediction.est
        print("Prediction for this movie: " + str(result))
    else:
        print("User or movie doesn't exist!")
