import pandas as pd
import warnings
from surprise import Dataset
from surprise import Reader
# from pathlib import Path
# data_folder = Path("hw1/data")
# ratings_file = data_folder / "ratings.dat"
# movies_file = data_folder / "movies.dat"
warnings.filterwarnings('ignore')

# This is the same data that was plotted for similarity earlier
# with one new user "E" who has rated only movie 1
# ratings_dict = {
#     "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
#     "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
#     "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
# }
print("Data is loading...")
ratings = pd.read_csv('ratings.dat', sep='::', names=['user_id','movie_id','rating','titmestamp'])

df = pd.DataFrame(ratings)
reader = Reader(rating_scale=(1, 5))

# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user_id", "movie_id", "rating"]], reader)
# Loads the builtin Movielens-100k data
movielens = Dataset.load_builtin('ml-100k')
print("Data is loaded.")

print("\n")
user_ids = ratings.user_id.unique().tolist()
movie_ids = ratings.movie_id.unique().tolist()
print('Number of Users: {}'.format(len(user_ids)))
print('Number of Movies: {}'.format(len(movie_ids)))
print("\n")