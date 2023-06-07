import random
import json

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def root() -> dict:
    return {'app': 'root'}


@app.get('/lat')
def get_random_latitude() -> str:
    return json.dumps({'latitude' : random.randint(0, 1)})


@app.get("/long")
def get_random_longitude() -> str:
    return json.dumps({'longitude' : random.randint(0, 1)})
