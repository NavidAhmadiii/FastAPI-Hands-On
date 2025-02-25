from enum import Enum
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()


@app.get("/", description="This is our first route")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.get("/users")
async def list_users():
    return {"message": "list users rout"}


@app.get("users/me")
async def get_current_user():
    return {"message": "this is current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    diary = "diary"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy."}

    if food_name.value == "fruits":
        return {"food_name": food_name,
                "message": "you are still healthy but like sweet things."}

    return {"food_name": food_name, "message": "I like chocolate milk"}


fake_items_db = [{"items_name": "Foo"}, {"items_name": "Bar"}, {"items_name": "Baz"}, ]


# @app.get("/items")
# async def list_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, sample_query_pram, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "sample_query_pram": sample_query_pram}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget."})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"user_id": user_id, "owner_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget."})
    return item


class Item(BaseModel):
    name: str
    descriptions: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
async def read_items(q: str | None = Query(
    None,
    min_length=3,
    max_length=10,
    title='sample  query string',
    description='this is a sample query',
    alias='item-query'
)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


@app.get("/items_hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}


@app.get("/items_validation/{item_id}")
async def read_items_validation(
        *,
        item_id: int = Path(..., title="The ID of the Item to get"),
        q: str,
        size: float = Query(..., gt=0, lt=7.75)
):
    result = {"item_id": item_id, "size": size}
    if q:
        result.update({"q": q})
    return result
