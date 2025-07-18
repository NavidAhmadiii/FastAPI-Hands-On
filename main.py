from datetime import datetime, time, timedelta
from enum import Enum
from typing import Literal, Union
from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile, HTTPException, Request, \
    Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import ResponseValidationError
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException

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

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []
#
#
# items = {
#     "foo": {
#         "name": "Foo", "price": 50.2
#     },
#     "bar": {
#         "name": "Bar", "description": "The description", "price": 62, "tax": 20.2
#     },
#     "baz": {
#         "name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []
#     },
# }
#
#
# @app.post('/items', response_model=Item, response_model_exclude_unset=True)
# async def create_item(item: Item):
#     return item
#
#
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
#
# @app.post('/user', response_model=UserOut)
# async def create_user(user: UserIn):
#     return user
#
#
# @app.get('/items/{item_id}/name', response_model=Item, response_model_include={'name', 'description'})
# async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]
#
#
# @app.get('/items/{item_id}/public', response_model=Item, response_model_exclude={'tax'})
# async def read_item_public_data(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# Part 14: Extra Models


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(BaseModel):
#     pass
#
#
# class UserInDB(UserBase):
#     hashed_password: str
#
#
# def fake_password_hasher(raw_password: str):
#     return f"supersecret{raw_password}"
#
#
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print(
#         UserInDB(
#             username="user.name123",
#             email="hello@hello.com",
#             hashed_password="password",
#             hello="world",
#             foo="bar"
#         )
#     )
#     print("User Save.")
#     return user_in_db
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_save = fake_save_user(user_in)
#     return user_save
#
#
# class BaseItem(BaseModel):
#     description: str
#     type: str
#
#
# class CarItem(BaseItem):
#     type: str = "car"
#
#
# class PlaneItem(BaseItem):
#     type: str = "Plane"
#     size: int
#
#
# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {"description": "Music is my favorite.", "type": "plane", "size": 5},
# }
#
#
# @app.get("/items/item_id", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]
#
#
# class ListItem(BaseModel):
#     name: str
#     description: str
#
#
# list_items = [
#     {"name": "Foo", "description": "There comes my hero."},
#     {"name": "Red", "description": "Its my aeroplanes."},
# ]
#
#
# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#     return list_items
#
#
# @app.get("/arbitrary/", response_model=dict[str, float])
# async def get_arbitrary():
#     return {"Foo": 1, "Bar": 2}


#  Part 15: Response Status Codes

#
# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name", name}
#
#
# @app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#     print("pk", pk)
#     return pk
#
#
# @app.get("/items/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
# async def read_item_redirect():
#     return {"hello": "world"}


# Part 16: Form Fields

#
# # Form Field
# @app.post("/login/")
# async def login(username: str = Form(...), password: str = Form(...)):
#     print("password: ", password)
#     return {"username": username}
#
#
# # Json field
# @app.post("/login-json/")
# async def login_json(username: str = Body(...), password: str = Body(...)):
#     print("password: ", password)
#     return {"username": username}


# Part 17: Request Files
# @app.post("/file/")
# async def create_file(files: list[bytes] = File(..., description="a file read as a byte")):
#     return {"file_sizes:": [len(file) for file in files]}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(files: list[UploadFile] = File(..., description="a file read as UploadFile")):
#     return {"filename:": [file.filename for file in files]}

# Part 18: Request Forms and Files
# @app.post("/files/")
# async def create_files(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type
#     }


# Part 19: Handling Errors
#
# items = {"foo": "The Foo wrestlers"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found.", headers={
#             "X-Error": "There are many error."})
#     return {"item": items[item_id]}
#
#
# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
#
#
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exception: UnicornException):
#     return JSONResponse(
#         status_code=status.HTTP_418_IM_A_TEAPOT,
#         content={"message": f"Oops {exception.name} did something.There goes a Rainbow..."})
#
#
# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}
#
#
# @app.exception_handler(ResponseValidationError)
# async def validations_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)
#
#
# @app.exception_handler(StarletteHTTPException)
# async def validations_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @app.get("/validation_item/{item_id}")
# async def read_validation_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="Nope I Don't Like 3.")
#     return {"item_id": item_id}
#
#
# @app.exception_handler(ResponseValidationError)
# async def validations_exception_handler(request: Request, exc: ResponseValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
#     )
#
#
# class Item(BaseModel):
#     title: str
#     size: int
#
#
# @app.get("/items")
# async def create_item(item: Item):
#     return item


# Part 20: Path Operation Configuration
#
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#
#
# class Tags(Enum):
#     items = "items"
#     users = "users"
#
#
# @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=[Tags.items],
#           summary="Creat an Item")
# # description="Create an Item with all information: name; description; price; tax; and a set of unique tags")
# async def create_item(item: Item):
#     """
#     Create an Item with all information:
#
#     - **name**: each item have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tags string for this item
#     """
#     return item
#
#
# @app.get("/items", tags=[Tags.items])
# async def read_items():
#     return [{"name": "foo", "price": 42}]
#
#
# @app.get("/users", tags=[Tags.users])
# async def read_users():
#     return [{"username": "phoebeBuffy"}]
#
#
# @app.get("/elements/", tags=Tags.items)
# async def read_elements():
#     return [{"item_id": "Foo"}]


# Part 21: JSON Compatible Encoder and Body Updates
# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.5
#     tags: list[str] = []
#
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 18, "tags": []},
# }
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items.get(item_id)
#
#
# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoder = jsonable_encoder(item)
#     items[item_id] = update_item_encoder
#     return update_item_encoder
#
#
# @app.patch("/items/{item_id}", response_model=Item)
# def patch_item(item_id: str, item: Item):
#     stored_item_data = items.get(item_id)
#     if stored_item_data is not None:
#         stored_item_model = Item(**stored_item_data)
#     else:
#         stored_item_model = Item()
#     update_data = item.dict()
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     print(item)
#     return updated_item


# Part 22: Dependencies - Intro

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}
#
#
# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons
#
#
# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons


# Part 23: Classes as Dependencies

# class Cat:
#     def __init__(self, name: str):
#         self.name = name
#
#
# fluffy = Cat("Mr Fluffy")
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# class CommonQueryPrams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit

# @app.get("/items")
# async def read_items(commons=Depends(CommonQueryPrams)):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip: commons.skip + commons.limit]
#     response.update({"items": items})
#     return response


# Part 24: Sub-Dependencies

# def query_extractor(q: str | None = None):
#     return q
#
#
# def query_or_body_extractor(q: str = Depends(query_extractor), last_query: str | None = Body(None)):
#     if q:
#         return q
#     else:
#         return last_query
#
#
# @app.post("/item")
# async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
#     return {"q-or_body": query_or_body}


# Part 25: Dependencies in path operation decorators, global dependencies

# async def verify_token(x_token: str = Header(...)):
#     if x_token != "fake-suer-secret-token":
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Token header invalid")
#
#
# async def verify_key(x_key: str = Header(...)):
#     if x_key != "fake-suer-secret-key":
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-key header invalid")
#     return x_key
#
#
# @app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [
#         {"item": "foo"},
#         {"item": ""}
#     ]
#
#
# @app.get("/users", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_users():
#     return [
#         {"username": "Nick"},
#         {"username": "Morty"},
#     ]

# Part 26: Security

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

fake_user_db = {
    "john": dict(
        username="johndoe",
        full_name="John Doe",
        email="john@example.com",
        hashed_passwrd="fakehashedsecret",
        disabled=False
    ),
    "alice": dict(
        username="alice",
        full_name="Alice Ahmadi",
        email="alice@example.com",
        hashed_passwrd="fakehashedsecret2",
        disabled=True
    ),
}


def fake_hash_password(password: str):
    return f"fakehaash{password}"


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decod_token(token):
    return get_user(fake_user_db, token)


async def get_current_user(token: str = Depends(oauth2_schema)):
    user = fake_decod_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user


@app.post("/token/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_user_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="incorrect username or password"
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="incorrect username or password"
        )
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me/")
async def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get('/items/')
async def read_items(token: str = Depends(oauth2_schema)):
    return {"token": token}
