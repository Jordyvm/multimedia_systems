import pandas as pd
import numpy as np
import warnings
from pathlib import Path
data_folder = Path("hw1\data")
ratings_file = data_folder / "ratings.dat"
movies_file = data_folder / "movies.dat"
warnings.filterwarnings('ignore')


user = 1
predict_movie = 1

data = pd.read_csv(ratings_file, sep='::', names=['user_id','movie_id','rating','titmestamp'])
# movies = pd.read_csv('movies.dat', sep='::', names=['movie_id','movie_title','genre'])
# print(data.head)

targetUser = pd.DataFrame(data.groupby('user_id')['movie_id'].sum())
print(targetUser.head())

# movie_names = pd.read_csv('movies.dat', sep=';;',error_bad_lines=False)
# print(movie_names.head())

# ratings = pd.DataFrame(data.groupby('movie_id')['rating'].mean())
#
# ratings['number_of_ratings'] = data.groupby('movie_id')['rating'].count()
