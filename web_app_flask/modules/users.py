import uuid
from faker import Faker

fake = Faker()
class User: 
  def __init__(self, username, email) -> None:
    self.id = str(uuid.uuid4())
    self.username = username
    self.email = email
  def update(self, username = None, email = None):
    if username: self.username = username
    if email: self.email = email

def generate_random_user():  
  username = fake.first_name()
  email = fake.email()

  return username, email

def generate_users():
  username, email = generate_random_user()
  return User(username, email)

def find_user(user_id):
  def fn(user):
    return user.id == user_id
  return fn

users = [generate_users() for _ in range(5)]

def add_user(username, email):
  users.append(User(username, email))

def remove_user(user):
  users.remove(user)
