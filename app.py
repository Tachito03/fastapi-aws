from fastapi import FastAPI
from routes.email import email 

app = FastAPI();
app.include_router(email)