from fastapi import FastAPI, HTTPException
from app.models import BookRequest
from app.services import get_book_image, get_similar_books
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI()


# Configure CORS (Cross-Origin Resource Sharing) to allow requests from specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers in requests
)

@app.post("/get_book_image/")
async def book_image(request: BookRequest):
    """
    Endpoint to retrieve the image URL of a book based on its title.
    
    Args:
        request (BookRequest): The request body containing the book title.
    
    Returns:
        JSON response with the image URL if found, otherwise raises a 404 error.
    """
    image_url = get_book_image(request.title)
    if image_url:
        return {"image": image_url}
    # Raise an HTTP 404 error if the book is not found
    raise HTTPException(status_code=404, detail="Book or user not found")

@app.post("/get_similar_books/")
async def similar_books(request: BookRequest):
    """
    Endpoint to retrieve a list of books similar to the given title.
    
    Args:
        request (BookRequest): The request body containing the book title.
    
    Returns:
        JSON response with a list of similar books, each containing title, similarity score, and image URL.
        Raises a 404 error if no similar books are found or if the book title is not in the database.
    """
    try:
        similar = get_similar_books(request.title)
        return {"similar_books": similar}
    except ValueError as e:
        # Raise an HTTP 404 error if no similar books are found or another issue occurs
        raise HTTPException(status_code=404, detail=str(e))

