from fastapi import FastAPI
from util import add_to_db, get_recs

app = FastAPI()


@app.get("/get_recs")
def read_root(s: str):
    return get_recs(s)

@app.get('/update_db')
def update_db(s: str):
    return add_to_db(s)