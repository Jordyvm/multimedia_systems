from surprise import KNNWithMeans

# Options for using user-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": True
}
algo = KNNWithMeans(sim_options=sim_options)
