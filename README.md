# News Project

This is a Flask application for managing news articles. The application allows users to view a list of news articles and add new articles through a simple web interface. Articles are stored in JSON format for easy access and manipulation.

## Project Structure

```
news_project
├── app.py                # Main entry point of the Flask application
├── static
│   └── style.css        # CSS styles for the application
├── templates
│   ├── index.html       # Template for displaying articles
│   └── add_article.html  # Template for adding new articles
├── articles
│   └── articles.json     # JSON file storing news articles
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```
   pip install Flask
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Usage

- To view the list of news articles, navigate to the home page.
- To add a new article, click on the "Add Article" link and fill out the form.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.