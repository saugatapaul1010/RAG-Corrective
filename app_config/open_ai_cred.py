import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")
