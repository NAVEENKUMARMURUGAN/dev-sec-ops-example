# Example 1: Weak Cryptography (B303)
# Safe version
import hashlib
hash = hashlib.sha256() 

# Example 2: Assert Usage in Production (B101)
# Safe version
def process_data_safe(data):
    if data is None:
        raise ValueError("Data cannot be None")
    return data.process()