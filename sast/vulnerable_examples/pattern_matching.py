# Example 1: Hardcoded Secrets (CWE-798)
API_KEY = "1234-abcd-5678-efgh"  # Vulnerable
PASSWORD = "admin123"  # Vulnerable

# Example 2: Dangerous Pickle Usage (B301)
import pickle
def load_data(data):
    return pickle.loads(data)  # Vulnerable