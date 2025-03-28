from datetime import datetime, time, timedelta
from enum import Enum
from typing import Literal

from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID

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

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item.",
#                 "price": 16.25,
#                 "tax": 1.67,
#             }
#         }
#
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {"item_id": item_id, "item": item}
#     return result


#  Part 11: Extra Data Types
# @app.put("/items/{item_id}")
# async def read_item(item_id: UUID, start_date: datetime | None = Body(None),
#                     end_time: datetime | None = Body(None),
#                     repeat_at: time | None = Body(None),
#                     process_after: timedelta | None = Body(None)):
#     start_process = start_date + process_after
#     duration = end_time - start_process
#     return {"item_id": item_id,
#             "start_date": start_date,
#             "end_date": end_time,
#             "repeat_at": repeat_at,
#             "process_after": process_after,
#             "start_process": start_process,
#             "duration": duration
#     }


# Part 12: Cookie and Header Parameters

# @app.get("/items")
# async def read_item(
#         cookie_id: str | None = Cookie(None),
#         accept_encoding: str | None = Header(None),
#         sec_ch_u: str | None = Header(None),
#         user_agent: str | None = Header(None),
#         x_token: list[str] | None = Header(None)
# ):
#     return {"cookie_id": cookie_id,
#             "Accept_Encoding": accept_encoding,
#             "sec-ch-u": sec_ch_u,
#             "User-Agent": user_agent,
#             "X-Token Values": x_token,
#             }


# Part 13: Response Model

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {
        "name": "Foo", "price": 50.2
    },
    "bar": {
        "name": "Bar", "description": "The description", "price": 62, "tax": 20.2
    },
    "baz": {
        "name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []
    },
}


@app.post('/items', response_model=Item, response_model_exclude_unset=True)
async def create_item(item: Item):
    return item


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


@app.post('/user', response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get('/items/{item_id}/name', response_model=Item, response_model_include={'name', 'description'})
async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]


@app.get('/items/{item_id}/public', response_model=Item, response_model_exclude={'tax'})
async def read_item_public_data(item_id: Literal["foo", "bar", "baz"]):
    return items[item_id]
