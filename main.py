import fastapi as _fastapi
from routers import Blockchain

app = _fastapi.FastAPI(
    title="Blog creator",
    description="Simple Blockchain API users can store data as block chains",
    contact={
        "name": "Ahmed Ali",
        "email": "ahmedalibalti2000@gmail.com"
        })


app.include_router(Blockchain.router, prefix="/Blockchain",tags=["Blockchain"])



