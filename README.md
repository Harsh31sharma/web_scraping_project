🛒 Flipkart Product Review Scraper (Flask App)
This is a simple Flask web application that scrapes product reviews from Flipkart based on a user's search query. It uses BeautifulSoup for web scraping and requests/urllib to fetch HTML content.

🔧 Features
Search for any product on Flipkart.

Fetches and displays:

Reviewer names

Ratings

Review content

Clean and simple HTML rendering using Jinja2 (render_template).

Error handling for missing queries, products, or reviews.

🧰 Tech Stack
Backend: Python, Flask

Web Scraping: BeautifulSoup, urllib, requests

Frontend: Jinja2 templates (home.html, results.html)

🚀 Getting Started
Prerequisites
Python 3.x


🧪 Example
Search: iphone 14
Output: ->Product link to Flipkart
        ->List of reviewer names, ratings, and review text
