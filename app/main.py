from pydantic import BaseModel
import pyrebase
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


if os.getenv('ENVIRONMENT') == 'production':
    load_dotenv('.env')
elif os.getenv('ENVIRONMENT') == 'development':
    load_dotenv('.env.dev')


firebaseConfig = {
    "apiKey": os.getenv('API_KEY'),
    "authDomain":  os.getenv('AUTH_DOMAIN'),
    "projectId":  os.getenv('PROJECT_ID'),
    "storageBucket":  os.getenv('STORAGE_BUCKET'),
    "messagingSenderId":  os.getenv('MESSAGING_SENDER_ID'),
    "appId":  os.getenv('APP_ID'),
    "measurementId":  os.getenv('MEASUREMENT_ID'),
    "databaseURL":  os.getenv('DATABASE_URL'),
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    email: str
    password: str

@app.post("/register")
async def register(newUser : User):
    try:
        auth.create_user_with_email_and_password(newUser.email, newUser.password)
        return {"message": "User created successfully"}
    except Exception as error:
        print(error)
        return {"message": "User already exists"}
    

@app.post("/login")
async def login(user : User):
    try:
        auth.sign_in_with_email_and_password(user.email, user.password)
        return {"message": "User logged in successfully"}
    except:
        return {"message": "Invalid credentials"}

@app.post("/test")
async def test():
    return {"message": "Test successful"}

if __name__ == "__main__":
    import uvicorn
    load_dotenv('.env.dev')
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    