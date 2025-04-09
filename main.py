from fastapi import FastAPI
from util import get_recs

app = FastAPI()


@app.get("/get_recs")
def read_root(s: str):
    return get_recs(s)