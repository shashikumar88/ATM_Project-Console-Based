accounts = {
    1001:[1000,2408,"user1@gmail.com","user1"],
    1002 : [2000,1234,"user2@gmail.com","user2"],
    1003 : [10000,None,"user3@gmail.com","user3"]
    }
print("********************************************")
while True:
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Pin Generate/Reset Pin")
    print("4.Mini Statement")
    print("5.Exit")
    opt=int(input("Choose the Option:"))
    print("********************************************")    
    if opt==1:
        print("********************************************")
        acc=int(input("Enter the Account Number:"))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is None:
                print(f"Dear {accounts[acc][3]} Pin not Generated!")
            else:
                pin=int(input("Enter your pin:"))
                if accounts[acc][1] == pin:
                    amount=int(input("Enter the amount:"))
                    if amount <= accounts[acc][0]:
                        accounts[acc][0] -= amount
                        print("Transaction Successfully Completed!")
                    else:
                        print("Insufficient Balance")
                else:
                    print(f"Dear {accounts[acc][3]} Please Enter the Correct pin Try Again!")
        print("********************************************")
    
    elif opt==2:
        acc=int(input("Enter the Account Number:"))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            amount=int(input("Enter the Amount:"))
            accounts[acc][0] += amount
            print("Deposit Successful!")
        print("********************************************")
    
    elif opt==3:
        print("********************************************")
        acc=int(input("Enter the Account Number:"))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is not None:
                print(f"Dear {accounts[acc][3]}, Do you want to change pin?")
                choice=int(input("Enter 1 for yes or 0 for no:"))
                if choice==1:
                    Current_Pin=int(input("Enter your Current Pin:"))
                    if accounts[acc][1] == Current_Pin:
                        New_Pin=int(input("Enter the New Pin:"))
                        if New_Pin == Current_Pin:
                            print("Current Pin and New Pin cannot be same!")
                        elif len(str(New_Pin)) > 4:
                            print("Pin must not be more than four Digits")
                        elif len(str(New_Pin)) < 4:
                            print("Pin must be four Digits")
                        else:
                            accounts[acc][1] = New_Pin
                            print("Pin Changed Successfully!")
                    else:
                        print("Invalid Current Pin")
                else:
                    print("Thank You Visit Again!")
            else:
                New_Pin=int(input("Enter your New Pin:"))
                if len(str(New_Pin)) > 4:
                    print("Pin must not be more than four Digits")
                elif len(str(New_Pin)) < 4:
                    print("Pin must be four Digits")
                else:
                    accounts[acc][1] = New_Pin
                    print("Pin Generated Successfully!")
        print("********************************************")
    
    elif opt==4:
        acc=int(input("Enter the Account Number:"))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            print("********************************************")
            print(f"Balance: {accounts[acc][0]}")
            print(f"Email: {accounts[acc][2]}")
            print(f"Username: {accounts[acc][3]}")
            print("********************************************")
    
    elif opt==5:
        print("Thank you for using our service!")
        break
    
    else:
        print("Invalid Option, please choose a valid option!")
        print("********************************************")
