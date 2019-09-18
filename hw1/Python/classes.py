# A simple rating data holder
class Rating:
    user = -1
    movie = -1
    score = -1

    def __init__(self, parts):
        self.user = int(parts[0])
        self.movie = int(parts[1])
        self.score = int(parts[2])

# An even simpler user data holder
class User:
    id = -1
    index = -1

    def __init__(self, userID, ratingIndex):
        self.id = userID;
        self.index = ratingIndex;