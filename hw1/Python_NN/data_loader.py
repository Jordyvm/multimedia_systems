import pandas as pd
import warnings
from surprise import Dataset
from surprise import Reader
warnings.filterwarnings('ignore')

print("Data is loading...")
# Loading in the rating data
ratings = pd.read_csv('data/ratings.dat', sep='::', names=['user_id','movie_id','rating','titmestamp'])

# Creating the pd dataframe
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
