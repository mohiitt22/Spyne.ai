from project import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# We will not use a secret key for this example
# app.secret_key = 'your_secret_key'  # Not set

# Dummy user database (just for demonstration purposes)
users_db = {
    "user@example.com": {
        "password": "password123"
    }
}

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Sign Up route
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Add basic validation
        if password != confirm_password:
            return "Passwords do not match!"

        # Add user to 'database' (for demonstration purposes)
        if email in users_db:
            return "User already exists!"
        
        users_db[email] = {'name': name, 'password': password}
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login route
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        password = request.form['password']

        # Check user credentials
        if email in users_db and users_db[email]['password'] == password:
            return redirect(url_for('index'))
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
