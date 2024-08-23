import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess the dataset
df = pd.read_csv("bbdd_ratings.csv")
df.dropna(subset=["image"], inplace=True)  # Remove rows where 'image' is NaN
df.rename(columns={'review/score': 'review'}, inplace=True)  # Rename 'review/score' to 'review'
df['review'] = df['review'].astype(int)  # Convert 'review' column to integer type

# Inspect review value distribution and first few records
print(df['review'].value_counts().sort_index())
print(df.head())

# Create item-user matrix
iu = df.pivot_table(index='Id', columns='User_id', values='review', fill_value=0)

# Preserve image information for each item (Id)
images = df[['Id', 'image']].drop_duplicates().set_index('Id')

# Calculate item similarity using cosine similarity
item_similarity = cosine_similarity(iu.to_numpy())

# Create the recommendation matrix
recommendation_matrix = pd.DataFrame(item_similarity, index=iu.index, columns=iu.index)

# Convert the matrix to long format for easier use
recommendation_matrix_long = recommendation_matrix.stack().rename_axis(['id1', 'id2']).reset_index(name='similarity')
recommendation_matrix_long = recommendation_matrix_long[
    (recommendation_matrix_long['id1'] != recommendation_matrix_long['id2']) &
    (recommendation_matrix_long['id1'] < recommendation_matrix_long['id2'])
]

# Join images from 'id2' to the recommendation matrix
recommendation_matrix_long = recommendation_matrix_long.join(images, on='id2')

# Save the recommendation matrix to disk
recommendation_matrix_long.to_pickle("matriz_recomendaciones_long.pkl")

