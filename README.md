
This project includes

flask <br>
python3.7 <br>
CSS:
- Bootstrap
<br>
flask-sqlalchemy = ORM <br>
flask-wtf = wtforms <br>
============================= <br>
<h2>Creating the database</h2> <br>

```python
>>> from app import db
>>> db.create_all()
```

Add User to Database
```python
>>> from app import User
>>> user_1 = User(username='Daniel', email='Daniel@dan.com', password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='Josh', email='Josh@dan.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
````
Querying the database
```python
>>> User.query.all()
[User('Daniel', 'Daniel@dan.com', 'default.jpg), User('Josh', 'Josh@dan.com', 'default.jpg)]
>>>
>>> User.query.filter_by(username='Josh').all()
[User('Josh', 'Josh@dan.com', 'default.jpg)]

```

Adding posts to a user
```python
>>> user = User.query.filter_by(username='Josh').first()
>>> user.id
2
>>> user.email
'Josh@dan.com'
>>> user.password
'password'
>>> user.image_file
'default.jpg'
>>> user.posts
[]
>>> post_1 = Post(title='Blog 1', content='First post concent!', user_id=user.id)
>>> post_2 = Post(title='Blog 2', content='Second Post concent!', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1', '2019-03-16 03:47:50.163513'), Post('Blog 2', '2019-03-16 03:47:50.167985')]
>>> post = Post.query.first()
>>> post.author
User('Josh', 'Josh@dan.com', 'default.jpg)

```

Delete your tables and data
```python
>>> db.drop_all() #removes all tables and data in the tables
>>> db.create_all() #creates our tables
>>> User.query.all()
[]
```
