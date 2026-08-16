from devices import register_devices, device_detail, update_device, delete_device
from auth import register_users, user_verification, show_all_users

def main():
  exit = 0
  while(exit == 0):
    print("select a option")
    print("1: register user")
    print("2: login")
    print("3: register device")
    print("4: show device")
    print("5: update device")
    print("6 delete device")
    print("7 show all users")
    print("8: exit")

    value = int(input("select your option"))

    match value:
        case 1:
            a = input(str("enter user id"))
            b = input(str("enter user name")) 
            c = input(str("user password"))         
            print(register_users(a,b,c))
        case 2:
            a = input(str("enter user id"))
            b = input(str("enter user name")) 
            c = input(str("user password"))         
            print(user_verification(a,b,c))
        case 3:
            a = input(str("enter user id"))
            b = input(str("enter device type")) 
            c = input(str("enter device status"))         
            print(register_devices(a,b,c))
        case 4:
            a = input(str("enter device id"))
            print(device_detail(a))
        case 5:
            device_id = input("enter device id ")
            device_type = input("enter device type ")
            device_status = input("enter device status ")
            print(update_device(device_id, device_type, device_status))
        case 6:
            device_id = input("enter device id you want to delete")
            print(delete_device(device_id))    

        case 7:
            print(show_all_users())

        case 8:
            exit = 1   