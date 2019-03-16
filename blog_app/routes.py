from flask import render_template, url_for, flash, redirect, request
from blog_app.models import User, Post
from blog_app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from blog_app import app, db, bcrypt

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
def home():
    return render_template('home.html', 
                            posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', 
                            title="About")

@app.route("/register", methods =['GET', 'POST'])
def register():
    # returns user to login if already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    
    ### POST #####################
    if form.validate_on_submit():
        #do not store passwords in database without salting and hashing
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        #create User in database
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been created! You are now able to log in','success') 
        
        #success is bootstrap class
        return redirect(url_for('login'))
    #### END POST ####################


    ### GET ################

    return render_template('register.html', 
                            title='Register', 
                            form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    # returns user to login if already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    ###### POST ##########################
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
            
        #checks if email is in database and
        #checks if passwored entered is correct
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #if they checked the remember me, it will remember
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email or password', 'danger')
    ##### END POST #######################
    #GET
    return render_template('login.html',
                        title ='Login',
                        form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")