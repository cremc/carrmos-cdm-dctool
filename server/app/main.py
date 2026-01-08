from fastapi import FastAPI
from .database import engine, Base
from .models import *

# Create tables
# In production, use Alembic for migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Qued Data Collection Tool API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Qued Data Collection Tool API"}

# We will import routers here as we build them.
# app.include_router(collect.router)
from .routers import academics, career, institution, general, ranking, finance, requirement, course, auth
app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(academics.router)
app.include_router(career.router)
app.include_router(institution.router)
app.include_router(general.router)
app.include_router(ranking.router)
app.include_router(finance.router)
app.include_router(requirement.router)
app.include_router(course.router)
