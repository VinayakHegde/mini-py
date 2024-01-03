from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html

class Doc:
  async def custom_swagger_ui_html(self):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="api doc")

  # Generate Swagger JSON
  async def get_open_api_endpoint(self, routes):
    return JSONResponse(content=get_openapi(title="Your API", version="1.0.0", routes=routes))
