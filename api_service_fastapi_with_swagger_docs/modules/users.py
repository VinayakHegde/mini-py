from pydantic import BaseModel

class User(BaseModel):
  name: str
  location: str

class Users:
  db = [
    {'id': 1, 'name': 'Alice', 'location': 'Wonderland'},
    {'id': 2, 'name': 'Bob', 'location': 'Boblandia'},
  ]

  def read_user(self, user_id: int):
    return next((u for u in self.db if u['id'] == user_id), None)

  def update_user(self, user_id: int, user: User):
    user_data = self.read_user(user_id=user_id)
    if user_data:
      user_data['name'] = user.name
      user_data['location'] = user.location

    return user_data
  
  def delete_user(self, user_id: int):
    user = self.read_user(user_id)
    if not user:
      return False
    self.db = [u for u in self.db if u['id'] != user_id]
    return True
  
  def read_users(self):
      return self.db

  def create_user(self, user: User):
    new_user = {
      'id': len(self.db) + 1,
      'name': user.name,
      'location': user.location,
    }
    self.db.append(new_user)
    return new_user

