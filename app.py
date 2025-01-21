from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Database model for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Routes and Views
@app.route('/')
def home():
    return render_template('index.html')  # Make sure this points to your login page

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Add the new user to the database
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('You have registered successfully!', 'success')
        return redirect(url_for('login'))  # Redirect to login page after successful registration

    return render_template('register.html')  # Renders registration form (register.html)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the database to check for valid user
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to dashboard after successful login
        else:
            flash('Invalid credentials. Please try again.', 'danger')  # Show error message if login fails

    return render_template('index.html')  # Renders login form (index.html)

@app.route('/dashboard')
def dashboard():
    # Simulating mockups (In the real application, fetch from the database)
    mockups = []  # Replace with actual logic to fetch mockups from the database
    return render_template('dashboard.html', mockups=mockups)

@app.route('/questions')
def questions():
    # Placeholder route for questions
    return render_template('questions.html')  # You'll need to create a questions.html file

@app.route('/upgrade')
def upgrade():
    # Placeholder route for upgrade
    return render_template('upgrade.html')  # You'll need to create an upgrade.html file

@app.route('/how_it_works')
def how_it_works():
    # Placeholder route for how it works
    return render_template('how_it_works.html')  # You'll need to create a how_it_works.html file

if __name__ == "__main__":
    app.run(debug=True)