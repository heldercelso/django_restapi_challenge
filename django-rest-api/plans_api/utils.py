# Use Python's built-in datetime module
from drf_yasg import openapi

post_response_schema_dict = {
    "201": openapi.Response(description="Example 201 response",
                            examples={"application/json": {"id": "int",}}
    ),
}

put_response_schema_dict = {
    "200": openapi.Response(description="Example 200 response",
                            examples={"application/json": {"id": "int",}}
    ),
}