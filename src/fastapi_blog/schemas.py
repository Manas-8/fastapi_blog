from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: EmailStr = Field(max_length=100)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    image_file: str | None 
    image_path: str

    model_config = ConfigDict(from_attributes=True)



class PostBase(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    content : str = Field(min_length=1)

class PostCreate(PostBase):
    user_id : int


from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    user_id: int
    date_posted: datetime
    author: UserResponse
