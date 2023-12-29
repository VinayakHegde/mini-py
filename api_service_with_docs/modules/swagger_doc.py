from flasgger import Swagger

version = 'v1'
base_path = f"/api/{version}"

template = {
  "swagger": "2.0",
  "info": {
    "title": "Flask RESTful + Swagger",
    "description": "Simple CRUD API service on Users",
    "contact": {
      "responsibleOrganization": "VinOrg",
      "responsibleDeveloper": "Vinayak Hegde",
      "email": "vinayak.nandi@gmail.com",
      "url": "https://github.com/VinayakHegde",
    },
    "version": version
  },
  "basePath": base_path,
  "schemes": [
    "http",
  ],
  "operationId": "vinorgopid"
}

swagger_config = {
  "headers": [],
  "specs": [
    {
      "endpoint": "spec",
      "route": f"{base_path}/spec.json",
      "rule_filter": lambda rule: True,  # all in
      "model_filter": lambda tag: True,  # all in
    }
  ],
  "static_url_path": "/flasgger_static",
  "swagger_ui": True,
  "specs_route": f"{base_path}/"
}

def generate_swagger(app):
  app.config['SWAGGER'] = {
    'title': template['info']['title']
  }
  return Swagger(app, template=template, config=swagger_config)
