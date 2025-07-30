import yaml
import os
from openai import OpenAI
from footchat.settings import OPENAI_API_KEY, CHATBOT_PROMPT

class ModelLoader:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.prompt = self.load_prompt()

    def load_prompt(self):
        return CHATBOT_PROMPT

    def get_client(self):
        return self.client

    def get_prompt(self):
        return self.prompt
