pin=1234
account_balance = 100000
account_number = 123456789
print("\t welcome to XYZ bank  ")
print('''1. view account balance 
2. case withdral 
3. case deposit 
4. pin change 
''')

Option = int(input("select task , want you perfome  :"))
if Option == 1 :
    user =int( input ("Enter your pin :"))
    if user == pin :
        print (f"your account balance is :  Rs{account_balance}")
    else :
        print( " Password is incorrect ")
elif Option==2 :
    money=int(input("Enter money you want to witdral ...."))
    if money<= 100000:
        withdal= int(input("enter your pin "))
        if withdal==pin:
            print("withdrol done...")
    else:
        print ("you don't have this money :::::")
elif Option==3:
    case=int(input("enter case diposit money  "))
    checkPAssword=int(input("Ener your password "))
    if checkPAssword==pin:
        account_balance+=case
        print(f"your account balance is {account_balance}")
    else:
        print("plese Enter your correct pin")
elif Option==4:
    old_password= int(input("enter your old password"))
    if old_password==pin:
        New_password=int(input("enter your new password."))
        pin=New_password
        print("your pin changed successfull ")
    else :
        print ("your pin is wrong .,.,.")

