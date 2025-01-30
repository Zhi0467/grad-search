from openai import OpenAI
from config import Config
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

API_KEY = Config.PERPLEXITY_API_KEY

# this function guides the user to find the right prompt
def query_perplexity_api_prompt(query, with_streaming = False):

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
                "Your job is to help the user to reflect on their statements by suggesting directions and asking detailed questions."
                "digging into their interests, academic and carrer plans etc."
                "each time you should output a concise paragraph summarizing what they want to search about, with details"
            ),
        },
        {   
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    if with_streaming:
        response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
        stream=True,
    )
    else:
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
        )
    return response

