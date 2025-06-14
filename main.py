from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id == 1:
        return {"item_id": 12, "q": q}
    else:
        return {"item_id": item_id, "q": q}
