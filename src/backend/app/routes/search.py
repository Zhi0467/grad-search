from flask import Flask, request, jsonify, render_template
from routes.search import Searcher
import logging
import os

# Initialize the Flask app
app = Flask(
    __name__,
    static_folder="../frontend/public",  # Path to the static files (CSS, JS, etc.)
    template_folder="../frontend/public"  # Path to the HTML templates
)
# Set up logging
logging.basicConfig(level=logging.INFO)

# Serve the chat interface
@app.route("/")
def home():
    return render_template("index.html")

# Handle chat requests
@app.route('/chat', methods=['POST'])
def search():
    logging.info("Received a POST request to /chat")
    data = request.json
    keyword = data.get("keyword")
    
    # Initialize the Searcher
    searcher = Searcher()
    
    # Get the ChatCompletion response from OpenAI
    chat_completion = searcher.prompt_chat_with_perplexity(keyword)
    
    # Extract the relevant data from the ChatCompletion object
    response_message = chat_completion.choices[0].message.content  # Extract the message content
    
    # Log the response
    logging.info(f"Response message: {response_message}")
    
    # Return the response as JSON
    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(debug=True)