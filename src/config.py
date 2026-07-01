import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API = os.getenv("GITHUB_API")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")