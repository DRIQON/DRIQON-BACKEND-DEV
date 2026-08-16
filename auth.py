from database import user
from sql_connection import connect_sql
import json

connection = connect_sql()
cursor = connection.cursor()

def load():
    with open("users.json", "r") as f:
       user = json.load(f)

def register_users(user_id, user_name, user_password):
    cursor.execute(
        """
        INSERT INTO users (user_id, user_name, user_password)
        VALUES (%s, %s, %s)
        """,
        (user_id, user_name, user_password)
    )

    connection.commit()

    return "User Registered"
      


def user_verification(user_id):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE user_id = %s
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    return user

def show_all_users():
    load()
    print(user)
    if len(user) == 0:
        return "No users found"

    for user_id in user:

        print(f"User ID: {user_id}")
        print(f"Name: {user[user_id]["user name"]}")
        print(f"Password: {user[user_id]["user password"]}")
        print("------------------------")

def delete_users(user_id):
    cursor.execute(
            """
            DELETE FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )
    
    connection.commit()
    
    return "user Deleted"



