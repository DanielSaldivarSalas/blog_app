from flask import Flask, render_template, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '14013659ae4a0a048de4a8054cea9096' #secrets.token_hex(16)

posts = [
    {
        'author': "Daniel Saldivar",
        'title': 'Blog Post 1',
        'content': "First post content",
        'date_posted': "April 20, 2018"
    },
    {
        'author': "Ryan Kramer",
        'title': 'Blog Post 2',
        'content': "Second post content",
        'date_posted': "April 21, 2018"
    }
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html', 
                            posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', 
                            title="About")

@app.route("/register")
def register():
    register_form = RegistrationForm()

    return render_template('register.html', 
                            title='Register', 
                            form=register_form)

@app.route("/login")
def register():
    login_form = LoginForm()
    return render_template('login.html',
                        title ='login',
                        form=login_form)

if __name__ == "__main__":
    app.run(debug=True)