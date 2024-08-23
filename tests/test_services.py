import pandas as pd
from app.services import get_book_image, get_similar_books


def test_get_book_image_success(mocker):
    df_mock = pd.DataFrame({
        'title': ['Harry Potter & the Prisoner of Azkaban'],
        'image': ['http://books.google.com/books/content?id=LbnwCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api']
    })

    def getitem_side_effect(key):
        return df_mock.__getitem__(key)
    
    mock_df = mocker.patch("app.services.df")
    mock_df.__getitem__.side_effect = getitem_side_effect

    image_url = get_book_image("Harry Potter & the Prisoner of Azkaban")
    assert image_url == "http://books.google.com/books/content?id=LbnwCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"



def test_get_book_image_not_found(mocker):
    mocker.patch("app.services.df", return_value=pd.DataFrame({
        'title': ['Harry Potter & the Prisoner of Azkaban'],
        'image': ['http://books.google.com/books/content?id=LbnwCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api']
    }))
    image_url = get_book_image("Libro No Existente")
    assert image_url is None

def test_get_similar_books_success(mocker):
    df_mock = pd.DataFrame({
        'id': [1, 2],
        'title': ["Harry Potter & the Prisoner of Azkaban", "Harry Potter and The Sorcerer's Stone"],
        'image': [
            'http://books.google.com/books/content?id=LbnwCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
            'http://books.google.com/books/content?id=HksgDQAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'
        ]
    })
    
    recommendation_matrix_mock = pd.DataFrame({
        'id1': [1],
        'id2': [2],
        'similitud': [0.19]
    })

def test_get_similar_books_no_similar(mocker):
    mocker.patch("app.services.df", return_value=pd.DataFrame({
        'id': [1],
        'title': ['Harry Potter & the Prisoner of Azkaban'],
        'image': ['http://books.google.com/books/content?id=LbnwCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api']
    }))
    mocker.patch("app.services.recommendation_matrix", return_value=pd.DataFrame())
    similar_books = get_similar_books("Harry Potter & the Prisoner of Azkaban")
    assert len(similar_books) == 0

