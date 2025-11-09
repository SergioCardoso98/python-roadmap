from fastapi import FastAPI

app = FastAPI()

#Normal GET request without params - also there is for POST, PUT, etc.. - https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get('/')
async def root():
    return {"message": "Hello World!"}

#Get with paremters + auto FastApi validation for int, it also allows None in this case
#And since returns int with will be "key": int (int withou "")
@app.get('/get_w_params/')
@app.get('/get_w_params/{param}')
async def get_w_params(param: int = None):
    return {"param": param}

#Get when we send and item with param in query, like http://127.0.0.1:8000/get_w_query_params?index=0
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get('/get_w_query_params')
async def get_w_query_params(index: int):
    return {"query_param_index_item": fake_items_db[0]}

