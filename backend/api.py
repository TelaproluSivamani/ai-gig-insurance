from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database.db_connection import get_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    phone: str
    platform: str
    city: str


@app.post("/register")
def register_user(user: User):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO workers (name, phone, platform, city)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (user.name, user.phone, user.platform, user.city))
    conn.commit()

    return {"message": "Worker Registered"}