# search.py
# This module implements the search functionality.
# It queries a synthetic database for matching entries based on a keyword. If no results are found, it queries the Google API.
# Input: A keyword (string) passed from the `app.py` endpoint.
# Output: A list of matching search results (from the database or Google API).

from backend.utils.perplexity_api import query_perplexity_api_prompt

class Searcher:
    def __init__(self, database=None):
        # Initialize with a synthetic database or a custom one
        self.database = database or [
            {"name": "Program A", "description": "Focused on AI."},
            {"name": "Program B", "description": "Neuroscience research."},
        ]

    def search_in_database(self, keyword):
        # Search in the synthetic database
        return [entry for entry in self.database if keyword.lower() in entry["description"].lower()]

    def prompt_chat_with_perplexity(self, keyword):
        return query_perplexity_api_prompt(keyword)


# Example usage
# searcher = Searcher()
# results = searcher.search_keyword("AI")
