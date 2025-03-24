import os
from dotenv import load_dotenv

load_dotenv()

print("GITHUB_TOKEN:", os.getenv("GITHUB_TOKEN"))
print("GITHUB_USERNAME:", os.getenv("GITHUB_USERNAME"))