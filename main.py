from typing import Union

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/posts")
def get_posts():
    return {"data": "these are your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    return {f"title:{payload['title']}, content: {payload['content']}"}
