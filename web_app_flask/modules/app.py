from flask import Flask, render_template, request, redirect, url_for
from .users import users, find_user, add_user, remove_user, generate_users
from .constants import routes, templates

app = Flask(__name__)

@app.route(routes['home'])
def home():
  return render_template(templates['home'], users = users)

@app.route(routes['view'])
def view(user_id):
  user = list(filter(find_user(user_id), users))
  print(user)
  return render_template(templates['view'], user=user[0], is_edit=False)


@app.route(routes['edit'], methods=['GET', 'POST'])
def edit(user_id):
  user = list(filter(find_user(user_id), users))[0]
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    user.update(username, email)
    return redirect(url_for('home'))
  return render_template(templates['view'], user=user, is_edit=True)

@app.route(routes['remove'])
def remove(user_id):
  user = list(filter(find_user(user_id), users))[0]
  remove_user(user=user)
  return redirect(url_for('home'))

@app.route(routes['add'], methods=['POST'])
def add():
  username = request.form['username']
  email = request.form['email']
  if username and email:
    add_user(username, email)
  return redirect(url_for('home'))

def start_web_app():
  app.run(debug=True)