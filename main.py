import uvicorn
import sqlite3
from fastapi import FastAPI, Request


app = FastAPI()
db = sqlite3.connect("main.db")
cursor = db.cursor()

@app.get("/enters/")
async def enters_get(request: Request):
    query = "SELECT count FROM customer_enters;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    return {
        "count": count
    }


@app.post("/enters/")
async def enters_post(request: Request):
    query = "SELECT count FROM customer_enters;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    data = await request.json()
    user_count = data.get("count") or 0
    query = f"UPDATE customer_enters SET count={count+user_count} WHERE id=1;"
    cursor.execute(query)
    db.commit()
    return {
        "message": "Saved."
    }


@app.get("/leaves/")
async def leaves_get(request: Request):
    query = "SELECT count FROM customer_leaves;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    return {
        "count": count
    }


@app.post("/leaves/")
async def leaves_post(request: Request):
    query = "SELECT count FROM customer_leaves;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    data = await request.json()
    user_count = data.get("count") or 0
    query = f"UPDATE customer_leaves SET count={count+user_count} WHERE id=1;"
    cursor.execute(query)
    db.commit()
    return {
        "message": "Saved."
    }


@app.get("/group_enters/")
async def group_enters_get(request: Request):
    query = "SELECT count FROM customer_group_enters;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    return {
        "count": count
    }


@app.post("/group_enters/")
async def group_enters_post(request: Request):
    query = "SELECT count FROM customer_group_enters;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    data = await request.json()
    user_count = data.get("count") or 0
    query = f"UPDATE customer_group_enters SET count={count+user_count} WHERE id=1;"
    cursor.execute(query)
    db.commit()
    return {
        "message": "Saved."
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
