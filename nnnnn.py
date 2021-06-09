user=input("Enter you user ID:")
password=input("Enter your password:")
if user=="sangeeta786":  
    if password=="9899":
         print("login suceccfully Welcome",user)
    else:
        print("Password is invild")       
elif user!="sangeeta786" and password=="9899":
    print("User id is not correct")
elif user=="sangeeta786" and password!="9899":
    print("Your password is worng")
elif user!="sangeeta786" and password!="9899":   
    print("Your user id or password is incorrect Please Create New Account:")
    newuser=input("Enter your new user ID:")
    newpassword=input("Enter your new password:")
    if newpassword>"a" and newpassword<"z" or newpassword>"9" or newpassword=="@#!%$&*/":
        print("Your password is strong")
        print("Your new account hasbeen create successfully")
    else:
        print("Your password is not strong")    


