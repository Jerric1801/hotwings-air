from flask import Flask, request, redirect, url_for, flash, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'guest' and password == 'guest':
            # In a real application, you would set a session cookie here
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # This is the secured page
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
