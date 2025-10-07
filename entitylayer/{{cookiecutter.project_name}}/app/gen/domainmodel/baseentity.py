from pydantic import BaseModel, Field


class BaseInputEntity(BaseModel):
    input:str = Field("", description="Input Argument")

class BaseOutputEntity(BaseModel):
    output:str = Field("", description="Output Argument")