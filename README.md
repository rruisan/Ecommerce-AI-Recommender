# AI-Powered Ecommerce Recommender

This project is a book recommendation system based on the similarity of user ratings. The project includes a web interface for users to search for books and receive recommendations, as well as an API built with FastAPI.

## Table of Contents

1. [Features](#1-features)
   - 1.1 [Web Interface](#11-web-interface)
   - 1.2 [API](#12-api)
   - 1.3 [Recommendation Algorithm](#13-recommendation-algorithm)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Usage](#4-usage)
5. [Tests](#5-tests)
   - 5.1 [Running Tests](#51-running-tests)
6. [Technologies Used](#6-technologies-used)
7. [Contributions](#7-contributions)
8. [License](#8-license)


# 1. Features

## 1.1. Web Interface

The web interface (`app/static/index.html`) allows the user to search for a book by its title. Once the title is entered, the book's image (if available) is displayed along with a list of recommended books similar to the searched book.

## 1.2. API

The API is built with FastAPI and exposes two main endpoints:

- **`/get_book_image/`**: Returns the image of a book based on the entered title.
- **`/get_similar_books/`**: Returns a list of books similar to the entered book, along with the image of each recommended book.

## 1.3. Recommendation Algorithm

The recommendation system works as follows:

1. Data Loading: A CSV file (`app/data/bbdd_ratings.csv`) containing user ratings for various books is loaded.

2. Preprocessing: The data is cleaned by removing rows that do not have associated images, and some columns are adjusted for easier processing.

3. Item-User Matrix Creation: A matrix is created where each row represents a book, each column represents a user, and the values are the ratings users have given to those books.

4. Similarity Calculation: The similarity between books is calculated using cosine similarity, which measures how close the ratings of two books are.

5. Recommendation Generation: A list of recommendations is generated for each book, including the image of the recommended book.

6. Storage: Finally, the list of recommendations is saved to a file for use by the application.

# 2. Prerequisites

- Python 3.7 or higher

# 3. Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rruisan/ecommerce-ai-recommender.git
    cd ecommerce-ai-recommender
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate     # On Linux/MacOS
    env\\Scripts\\activate      # On Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the recommendation matrix:

    ```bash
    python3 app/matrix_creation.py
    ```

5. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

6. Open `app/static/index.html` in your browser to use the application.

# 4. Usage

1. Open `app/static/index.html` in your browser.
2. Enter a book title in the search bar.
3. Click "Search".
4. The book's image will appear along with three recommendations of similar books.

![App Usage](app/static/assets/screenshot.png)

# 5. Tests

To ensure the project works correctly, automated tests have been created, which can be run using pytest. These tests validate the functionality of the main functions and services of the project.

## 5.1. Running Tests

1. Ensure you are in the virtual environment:

    ```bash
    source env/bin/activate     # On Linux/MacOS
    env\\Scripts\\activate      # On Windows
    ```

2. Install any development requirements found in **requirements.txt**.

3. Run the tests:

    ```bash
    PYTHONPATH=$(pwd) pytest
    ```

The tests are located in the `tests/` directory and include validations for the main modules, such as `test_main.py` and `test_services.py`.

# 6. Technologies Used

- **Python 🐍**: The core language used for development.
- **Scikit-learn 📊**: Utilized for implementing machine learning algorithms and similarity calculations.
- **FastAPI 🚀**: The web framework used for building the API.
- **HTML/CSS/JavaScript 🌐**: Used for the front-end interface.
- **Uvicorn ⚡**: ASGI server for running FastAPI.
- **Pytest 🧪**: For automated testing.

# 7. Contributions

Contributions are welcome. Feel free to open an **issue** or submit a **pull request** with improvements.

# 8. License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
