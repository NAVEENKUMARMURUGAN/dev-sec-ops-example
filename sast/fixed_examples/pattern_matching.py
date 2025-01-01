# Example 1: Hardcoded Secrets (CWE-798)
# Safe version
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")

# Example 2: Dangerous Pickle Usage (B301)
# Safe version
import json
def load_data_safe(data):
    return json.loads(data)