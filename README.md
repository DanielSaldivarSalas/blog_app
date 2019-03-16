
This project includes

flask <br>
python3.6 <br>
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
Get all Users in the database
```python
>>> User.query.all()
[User('Daniel', 'Daniel@dan.com', 'default.jpg), User('Josh', 'Josh@dan.com', 'default.jpg)]
>>>
>>> User.query.filter_by(username='Josh').all()
[User('Josh', 'Josh@dan.com', 'default.jpg)]
```
