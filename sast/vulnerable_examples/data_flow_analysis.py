# Example 1: Cross-Site Scripting (XSS)
@app.route('/profile')
def profile():
    username = request.args.get('user')
    return f"<h1>Profile for {username}</h1>"  # Vulnerable

# Safe version
from markupsafe import escape
@app.route('/profile')
def profile_safe():
    username = request.args.get('user')
    return f"<h1>Profile for {escape(username)}</h1>"

# Example 2: SQL Injection with Data Flow
def get_user_records(user_input):
    base_query = "SELECT * FROM users"
    if user_input:
        query = base_query + " WHERE name LIKE '%" + user_input + "%'"  # Vulnerable
    return db.execute(query)

# Safe version
def get_user_records_safe(user_input):
    query = "SELECT * FROM users WHERE name LIKE ?"
    return db.execute(query, ('%' + user_input + '%',))