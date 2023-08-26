from typing import Annotated

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, max_length=300
    )
    price: float = Field(gt=0)
    tax: float | None = None
    
class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(ge=0, le=1000)],
    item: Annotated[Item, Body(embed=True)]
    
):
    results = {"item_id": item_id, "item": item}
    return results
