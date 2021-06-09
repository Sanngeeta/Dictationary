print("WELCOME  TO  THE-LOGIN  OR  SIGN_UP  PAGE")


que=input("Do You Have Account(Y/N)? ")
if que=="y" or que=="Y":
    my_file=open("login_page.txt","w")

    name=input("Enter the username:")
    my_file.write(name)

    lastname=input("Enter the lastname:")
    my_file.write(lastname)

    pas=input("Enter the password:")
    my_file.write(pas)
    print("Loggon on succfully!")
    
    my_file.close()
else:
    num=input("DO YOU WANT SIGH_UP NEW ACCOUNT (YES/NO)?!")
    if num=="YES" or num=="yes":
        file=open("new_login.txt","w")
        new_user=input("Enter the new  username:")
        file.write(new_user)
        lastName=input("Enter the new lastname!")
        file.write(lastName)
        password=input("Enter the new password !")
        if len(password)>4 and len(password)<16:
            file.write(password)
            print("Your new account loggn on succfuly!")
        else:
            print("Your week password ! Thank you for trying !")
        file.close()
    else:
        print("Thank you for trying to sign up")

        

    