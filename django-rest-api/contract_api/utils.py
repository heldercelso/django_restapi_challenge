# Use Python's built-in datetime module
from datetime import date
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

def age(birthdate):
    # Get today's date object
    today = date.today()
    
    # A bool that represents if today's day/month precedes the birth day/month
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Calculate the difference in years from the date object's components
    year_difference = today.year - birthdate.year
    
    # The difference in years is not enough. 
    # To get it right, subtract 1 or 0 based on if today precedes the 
    # birthdate's month/day.
    
    # To do this, subtract the 'one_or_zero' boolean 
    # from 'year_difference'. (This converts
    # True to 1 and False to 0 under the hood.)
    age = year_difference - one_or_zero
    
    return age