from pydantic import BaseModel

# Define a model for a book request using Pydantic
class BookRequest(BaseModel):
    title: str  # The title of the book being requested

