from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from .swagger_doc import generate_swagger, base_path

app = Flask(__name__)
api = Api(app)

# Sample in-memory data for users
users = [
  {'id': 1, 'name': 'Alice', 'location': 'Wonderland'},
  {'id': 2, 'name': 'Bob', 'location': 'Boblandia'},
]

class UserResource(Resource):
  def get(self, user_id):
    """
    Get user by ID.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
    responses:
      200:
        description: A user by ID
    """
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
      return user
    else:
      return {'message': 'User not found'}, 404

  def put(self, user_id):
    """
    Update user by ID.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the user
            location:
              type: string
              description: The location of the user
    responses:
      200:
        description: The updated user
      404:
        description: User not found
    """
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
      return jsonify({'message': 'User not found'}), 404

    request_data = request.get_json()
    user['name'] = request_data.get('name', user['name'])
    user['location'] = request_data.get('location', user['location'])

    return jsonify(user)

  def delete(self, user_id):
    """
    Delete user by ID.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
    responses:
      200:
        description: User deleted successfully
    """
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted successfully'})

class UsersResource(Resource):
  """
  Users Resource for listing and adding users.
  """

  def get(self):
    """
    Get a list of all users.
    ---
    tags:
      - Users
    responses:
      200:
        description: A list of users
    """
    return jsonify(users)

  def post(self):
    """
    Add a new user.
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the user
            location:
              type: string
              description: The location of the user
    responses:
      200:
        description: The added user
    """
    request_data = request.get_json()
    
    # Validate that required fields are present in the request data
    if 'name' not in request_data or 'location' not in request_data:
      return jsonify({'error': 'Name and location are required fields'}), 400

    new_user = {
      'id': len(users) + 1,
      'name': request_data['name'],
      'location': request_data['location'],
    }
    users.append(new_user)
    return new_user, 201

# Add resources to the API
api.add_resource(UserResource, f'{base_path}/users/<int:user_id>')
api.add_resource(UsersResource, f'{base_path}/users')

def start_service():
  generate_swagger(app)
  app.run(debug=True)
