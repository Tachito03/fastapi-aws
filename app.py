from logging import Handler
from fastapi import FastAPI
from routes.email import email 
from mangum import Mangum

app = FastAPI();
app.include_router(email)

handler = Mangum(app=app)