# dependencies/db.py
from fastapi import Request

def get_db(request: Request):
    return request.app.state.db
