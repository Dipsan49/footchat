from ai_service.load_model import ModelLoader
from typing import Dict, Any
from footchat.settings import OPENAI_MODEL


class FootballChatbotEngine:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.client = self.model_loader.get_client()
        self.prompt = self.model_loader.get_prompt()
        self.model_name = OPENAI_MODEL

    def generate_response(self, user_query: str) -> Dict[str, Any]:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.prompt},
                    {"role": "user", "content": user_query}
                ]
            )
            content = response.choices[0].message.content.strip()

            return {
                "success": True,
                "response": content
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "response": None
            }
