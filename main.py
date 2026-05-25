from fastapi import FastAPI
from database import engine
from models import Base
from routes import auth_routes, sensor_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Agriculture API")

app.include_router(auth_routes.router)
app.include_router(sensor_routes.router)