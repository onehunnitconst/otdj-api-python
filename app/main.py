from fastapi import FastAPI
from users import user_router
from authentication import authentication_router
from db.database import Base, engine;

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(authentication_router.router)