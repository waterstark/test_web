from pydantic import BaseModel, StrictStr
from typing import Optional


class Post(BaseModel):
    id: int
    author_of_post: StrictStr

    class Config:
        orm_mode = True


class ReadAllPosts(BaseModel):
    data: list[Post]

    class Config:
        orm_mode = True


class CreatePost(BaseModel):
    data: Post

    class Config:
        orm_mode = True


class EditPost(BaseModel):
    author_of_post: Optional[StrictStr] | None

    class Config:
        orm_mode = True

class LikePost(BaseModel):
    