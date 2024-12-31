# Example 1: SQL Injection Vulnerability
def get_user(user_input):
    query = f"SELECT * FROM users WHERE id = {user_input}"  # Vulnerable
    cursor.execute(query)
    return cursor.fetchone()

# Example 2: Command Injection
def execute_command(user_input):
    os.system(f"echo {user_input}")  # Vulnerable

# Example 3: Hardcoded Credentials
API_KEY = "1234-abcd-5678-efgh"  # Vulnerable
PASSWORD = "admin123"  # Vulnerable

# Example 4: Path Traversal
def read_file(filename):
    with open(filename) as f:  # Vulnerable
        return f.read()

# Fixed versions of the above code
def get_user_safe(user_input):
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_input,))
    return cursor.fetchone()

def execute_command_safe(user_input):
    subprocess.run(["echo", user_input], check=True)

def read_file_safe(filename):
    safe_path = os.path.join(ALLOWED_DIR, filename)
    if not os.path.normpath(safe_path).startswith(ALLOWED_DIR):
        raise SecurityException("Path traversal detected")
    with open(safe_path) as f:
        return f.read() 