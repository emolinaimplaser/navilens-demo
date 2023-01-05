from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lines")
def read_item():
    return {"line": "line2","direction":"Casa de Papel", "time": str(random.randint(1, 6))}
