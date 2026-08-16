from database import user
from sql_connection import connect_sql

connection = connect_sql()
cursor = connection.cursor()
       
def register_devices(device_id, device_type, device_status):
    cursor.execute(
        """
        INSERT INTO devices (device_id, device_type, status)
        VALUES (%s, %s, %s)
        """,
        (device_id, device_type, device_status)
        )
    
    connection.commit()
    
    return "device register"
    


def device_detail(device_id):

    cursor.execute(
            """
            SELECT * FROM devices
            WHERE device_id = %s
            """,
            (device_id,)
        )
    
    user = cursor.fetchone()
    
    return user

     

def update_device(device_id, device_type, device_status):
    cursor.execute(
        """
        UPDATE devices
        SET
           device_type = %s,
           status = %s
        WHERE
           device_id = %s   
        """,
        (device_type, device_status, device_id)
         
       )
    connection.commit()

    return "device Updated"

def delete_device(device_id):

    cursor.execute(
        """
        DELETE FROM devices
        WHERE device_id = %s
        """,
        (device_id,)
    )

    connection.commit()

    return "Device Deleted"
