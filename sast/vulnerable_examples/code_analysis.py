# Example 1: Weak Cryptography (B303)
import md5  # Vulnerable
hash = md5.new()  

# Safe version
import hashlib
hash = hashlib.sha256()

# Example 2: Assert Usage in Production (B101)
def process_data(data):
    assert data != None  # Vulnerable
    return data.process()

# Safe version
def process_data_safe(data):
    if data is None:
        raise ValueError("Data cannot be None")
    return data.process()