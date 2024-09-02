correct_username="Abhishek"
correct_password="password123"

attempts=0

while attempts< 3:
    username=input("Enter your name")
    password=input("Enter your password")
    
    if username.strip().lower()==correct_username.lower()and password.strip()==correct_password:
        print("login successful")
        break
    else:
        print("incorrect usernme or password")

        attempts+=1

if attempts ==3:
    print("invalid   too many incorrect attempts")