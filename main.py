from typing import Optional, Union

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/posts")
def get_posts():
    return {"data": "these are your posts"}


@app.post("/posts")
def create_posts(post: Post):
    print(post.model_dump())
    return {"data": "post"}
