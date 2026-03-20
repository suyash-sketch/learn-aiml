from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name' : "foo"}, { "item_name" : "bar" }, { "item_name" : "baz" }]

# @app.get('/items/')
# async def read_items(skip : int = 0, limit : int = 10):
#     return fake_items_db[skip : skip + limit]

#Optional parameters
# @app.get('/items/{item_id}')
# async def read_items(item_id : str, q : str | None = None):
#     if q:
#         return { "item_id" : item_id, "q" : q }
#     return {"item_id" : item_id}

#query parameter type conversion
@app.get('/items/{item_id}')
async def read_item2(item_id : str, q : str | None = None, short : bool = False):
    item = {"item_id" : item_id}
    if q:
        item.update({"q" : q})
    if not short:
        item.update(
            {"description" : "This is an amazing item that has a long description"}
            )

    return item

# Multiple path and query parameters
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
    user_id : int, item_id : str, q : str | None = None, short : bool = False
    ):
    item ={ "item_id" : item_id, "owner_id" : user_id }
    if q:
        item.update({"q" : q})
    if not short:
        item.update({"description" : "This is an amazing item that has a long description" })

    return item










