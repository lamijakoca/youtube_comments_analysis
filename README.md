# YouTube Comments Analyzer

This is a Django application for analyzing YouTube video comments. It allows users to input a YouTube video URL and retrieve the top questions from the comments, sorted by the number of likes. 

## Features

- Fetch comments from a YouTube video using the YouTube Data API.
- Filter comments to identify questions.
- Sort questions by the number of likes.
- Display the top questions on a web page.

## Prerequisites

- Python 3
- Django 3 or higher
- YouTube Data API key
- `pip` for installing required packages

## Installation

1. Clone the repository

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory of your project and add your YouTube Data API key and other settings:

    ```plaintext
    SECRET_KEY=your-django-secret-key
    API_KEY=your-youtube-api-key
    ```

5. Run database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

1. Open the application in your browser.
2. Enter the URL of a YouTube video into the input form and submit.
3. The application will fetch comments from the video, filter out questions, and display the top questions based on the number of likes.
