# Funny Confetti Game Webapp

This is a simple web application that demonstrates:
1. A Python-built web server using only standard library modules
2. Integration of an external JavaScript game library
3. Dynamic content insertion from a README file

## How It Works

- The server is built with Python's `http.server` module
- It serves a simple HTML page with a confetti game
- The confetti game comes from the `confetti-js` library
- This README content is dynamically inserted into the page

## Requirements

- Python 3.x
- Web browser with JavaScript enabled

## Running the App

1. Execute `python server.py`
2. Your browser should open automatically
3. Click the button to see the confetti explosion!

## Customization

You can modify:
- The README.md file to change this content
- The index.html template (though keep the <!-- README_CONTENT --> marker)
- The server port in server.py
