from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(item_name: Annotated[list[str], Query()] = []):
    query_items = {"item_name": item_name}
    return query_items 
