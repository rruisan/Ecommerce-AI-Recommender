import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import difflib

# Load the dataset containing book ratings and metadata
df = pd.read_csv('app/data/bbdd_ratings.csv')

# Load the precomputed recommendation matrix from a file
with open('app/data/matriz_recomendaciones_long.pkl', 'rb') as f:
    recommendation_matrix = pickle.load(f)

def get_book_image(title: str) -> str:
    # Filter the dataset to find the row corresponding to the given title
    book = df[(df['title'] == title)]
    print(f"Filtered: {book}")  # Debugging: print the filtered DataFrame
    if not book.empty:
        # Return the image URL if the book is found
        return book.iloc[0]['image']
    # Return None if the book is not found
    return None

def get_similar_books(title: str):
    # Find the book by its title in the dataset
    book = df[df['title'] == title]
    if book.empty:
        # Return an empty list if the book is not found
        return []
    
    # Get the unique identifier (ID) of the found book
    book_id = book.iloc[0]['id']
    
    # Filter the recommendation matrix to find books similar to the given book ID
    similares = recommendation_matrix[(recommendation_matrix['id1'] == book_id) | 
                                       (recommendation_matrix['id2'] == book_id)]
    
    # Sort the similar books by their similarity score in descending order
    similares = similares.sort_values(by='similitud', ascending=False)
    
    similar_books = []
    seen_titles = set()  # Use a set to store already recommended titles
    for _, row in similares.iterrows():
        # Determine the ID of the similar book
        similar_id = row['id2'] if row['id1'] == book_id else row['id1']
        similar_title = df[df['id'] == similar_id]['title'].values[0]
        similar_image = df[df['id'] == similar_id]['image'].values[0]  # Get the image
        
        # Ensure the recommended title is not too similar to the original title
        if difflib.SequenceMatcher(None, title.lower(), similar_title.lower()).ratio() < 0.8:
            # Add only unique titles to the recommendation list
            if similar_title not in seen_titles:
                similar_books.append({
                    "title": similar_title,
                    "similarity": round(row['similitud'], 2),  # Round the similarity score to two decimal places
                    "image": similar_image  # Include the image URL in the response
                })
                seen_titles.add(similar_title)
        
        # Stop once 3 valid recommendations are obtained to limit the result size
        if len(similar_books) >= 3:
            break
    
    return similar_books

