from enum import Enum
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


# @app.get("/", description="This is our first route")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.post("/")
# async def post():
#     return {"message": "hello from the post route"}
#
#
# @app.put("/")
# async def put():
#     return {"message": "hello from the put route"}
#
#
# @app.get("/users")
# async def list_users():
#     return {"message": "list users rout"}
#
#
# @app.get("users/me")
# async def get_current_user():
#     return {"message": "this is current user"}
#
#
# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"user_id": user_id}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     diary = "diary"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy."}
#
#     if food_name.value == "fruits":
#         return {"food_name": food_name,
#                 "message": "you are still healthy but like sweet things."}
#
#     return {"food_name": food_name, "message": "I like chocolate milk"}
#
#
# fake_items_db = [{"items_name": "Foo"}, {"items_name": "Bar"}, {"items_name": "Baz"}, ]
#
#
# # @app.get("/items")
# # async def list_item(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip:skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_pram, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "sample_query_pram": sample_query_pram}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget."})
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"user_id": user_id, "owner_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"descriptions": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget."})
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     descriptions: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items")
# async def read_items(q: str | None = Query(
#     None,
#     min_length=3,
#     max_length=10,
#     title='sample  query string',
#     description='this is a sample query',
#     alias='item-query'
# )):
#     result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items_hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}
#
#
# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#         *,
#         item_id: int = Path(..., title="The ID of the Item to get"),
#         q: str,
#         size: float = Query(..., gt=0, lt=7.75)
# ):
#     result = {"item_id": item_id, "size": size}
#     if q:
#         result.update({"q": q})
#     return result

# class Item(BaseModel):
#     name: str
#     descriptions: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to fet", ge=0, le=150),
#         q: str | None = None,
#         item: Item = Body(..., embed=True),
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     return result

# # part 8 body fields
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(..., gt=0, title="The price must be greater then 0")
#     tax: float | None = None
#
#
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     result = {"item_id": item_id, "item": item}
#     return result


# part 9 body - nested field
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = []
#     image: list[Image] | None = None
#
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     item: list[Item]
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {'item_id': item_id, 'item': item}
#     return result
#
#
# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
#
# @app.post("/images/multiple")
# async def create_multiple_image(images: list[Image] = Body(..., embed=True)):
#     return images
#
#
# @app.post("/blah")
# async def create_some_blahs(blahs: dict[int, float]):
#     return blahs


# Part 10: Declare Request Example Data

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item.",
                "price": 16.25,
                "tax": 1.67,
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, "item": item}
    return result
