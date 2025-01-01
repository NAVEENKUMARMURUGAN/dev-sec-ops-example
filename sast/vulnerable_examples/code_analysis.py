# Example 1: Weak Cryptography (B303)
import md5  # Vulnerable
hash = md5.new()  

# Example 2: Assert Usage in Production (B101)
def process_data(data):
    assert data != None  # Vulnerable
    return data.process()