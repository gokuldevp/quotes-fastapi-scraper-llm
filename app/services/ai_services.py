from openai import OpenAI
from app.core.config import GEMINI_BASE_URL, GOOGLE_API_KEY, MODEL, SYSTEM_PROMPT

class AIService:
    def __init__(self):
        self.client = OpenAI(
            base_url=GEMINI_BASE_URL,
            api_key=GOOGLE_API_KEY
        )

    def get_user_prompt(self, content: str) -> str:
        user_prompt = f"""
        Here is the list of quotes on the website {content} - 
        respond with the full quote in JSON format.
        Do not include html tags or any other formatting, just the quote text, author, and tags.
        """
        return user_prompt

    def generate_quote(self, web_data: str) -> str:
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": self.get_user_prompt(web_data)}
            ],
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content