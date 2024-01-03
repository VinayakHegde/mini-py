from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .swagger_doc import Doc
from .users import Users

app = FastAPI()
doc = Doc()

# Sample in-memory data for users
users = Users()

class User(BaseModel):
  name: str
  location: str

# Route to get a user by ID
@app.get("/users/{user_id}", response_model=dict, tags=["Users"])
def read_user(user_id: int):
  user = users.read_user(user_id)
  if user:
    return user
  else:
    raise HTTPException(status_code=404, detail="User not found")

# Route to update a user by ID
@app.put("/users/{user_id}", response_model=dict, tags=["Users"])
def update_user(user_id: int, user: User):
  user_data = users.update_user(user_id)
  if not user_data:
    raise HTTPException(status_code=404, detail="User not found")

  return user_data

# Route to delete a user by ID
@app.delete("/users/{user_id}", response_model=dict, tags=["Users"])
def delete_user(user_id: int):
  if users.delete_user(user_id):
    return {'message': 'User deleted successfully'}
  return {'message': 'User not found'}
  

# Route to get all users
@app.get("/users", response_model=list, tags=["Users"])
def read_users():
  return users.read_users()

# Route to add a new user
@app.post("/users", response_model=dict, tags=["Users"], )
def create_user(user: User):
  return users.create_user(user)


# Include Swagger UI in the app
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
  return doc.custom_swagger_ui_html()

@app.get("/openapi.json", response_model=dict)
async def get_open_api_endpoint():
  return doc.get_open_api_endpoint(app.routes)

def start_service():
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)
