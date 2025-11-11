from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated

class UserInput(BaseModel):

    pressure: Annotated[float, Field(gt=800, lt=1200, description="Atmospheric pressure in hPa")]
    dewpoint: Annotated[float, Field(gt=-50, lt=30, description="Dewpoint temperature in Celsius")]
    humidity: Annotated[float, Field(gt=0, lt=100, description="Relative humidity in percentage")]
    cloud: Annotated[float, Field(gt=0, lt=100, description="Cloud cover in percentage")]
    sunshine: Annotated[float, Field(ge=0, le=24, description="Sunshine duration in hours")]
    winddirection: Annotated[float, Field(gt=1, lt = 360, description="Wind direction as compass points")]
    windspeed: Annotated[float, Field(gt=0, lt=150, description="Wind speed in km/h")]