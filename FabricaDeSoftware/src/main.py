from typing import Union
from fastapi import FastAPI

import Router

app = FastAPI()

global TOTAL_PARKING_SPOTS
TOTAL_PARKING_SPOTS = 50

@app.get(Router.GET_MAIN_API_LANDING)
def ping():
    return {"Ping": "Pong"}


@app.get(Router.GET_AVAILABLE_SPACES)
def available_spaces(cars_parked: int):
    return {"cars_parked": cars_parked, "available_spaces": TOTAL_PARKING_SPOTS - cars_parked}


@app.put(Router.PUT_TOTAL_SPACES)
def update_total_spaces(total_spaces: int):
    global TOTAL_PARKING_SPOTS
    TOTAL_PARKING_SPOTS = total_spaces
    return {"total_spaces": TOTAL_PARKING_SPOTS}
