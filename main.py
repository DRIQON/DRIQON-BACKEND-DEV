from devices import register_devices, device_detail, update_device, delete_device
from auth import register_users, user_verification, delete_users
from sql_connection import connect_sql
from menu import main
from fastapi import FastAPI
from firebase_config import firebase_connect, verify_token


app = FastAPI()
connect_sql()
firebase_connect()


@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/HEALTH")
def health():
    return {"message": "Your System Is healthy"}

@app.post("/REGISTER user")
def register(user_id: str, user_name: str, user_password: str):

    return register_users(user_id, user_name, user_password)

@app.post("/FIND user")
def find_user(user_id: str):
    return user_verification(user_id)

@app.post("/ DELETE User")
def delete(user_id: str):
    return delete_users(user_id)

@app.post("/REGISTER device")
def  register(device_id: str, device_type: str, device_status: str):

    return register_devices(device_id, device_type, device_status) 
    

@app.post("/device detail")
def register(device_id: str):
    return device_detail(device_id)



@app.post("/UPDATE device")
def register(device_id: str, device_type: str, device_status: str):
    return update_device(device_id, device_type, device_status)


@app.post("/DELETE device")
def delete_devices(device_id: str):
    return delete_device(device_id)


@app.post("/verify-token")
def verify(id_token: str):

    user = verify_token(id_token)

    if user is None:
        return "Invalid Token"

    return {
        "uid": user["uid"],
        "email": user.get("email")
    }

 
