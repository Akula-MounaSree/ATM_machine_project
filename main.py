from ATM_functions import check_balance, deposit_money, withdraw_money, transaction_history

#main function starts here
def menu():
    #using while loop
    while True:
        print("-----------ATM Machine-------------")
        print("____________________________________________")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        choice=input("Enter your Choice: ")

        if choice=="5": #taking 5th choice because the it takes to exit
            print("\n Thank you for using ATM Machine")
            break #exit the loop -- end program
        
        #using try and except to handling error 
        #account details

        name=input("enter the Name: ")
        try:
            pin=int(input("enter the PIN:"))
        except ValueError:
            print("PIN must be numeric.")
            continue #starts the loop

        #choice's
        if choice=="1":
            check_balance(name, pin)
        elif choice=="2":
            try:
                amount=int(input("enter the Deposit amount:"))
                deposit_money(name,pin,amount)
            except ValueError:
                print("\n Amount must be numeric.")
        elif choice=="3":
            try:
                amount=int(input("enter withdraw amount:"))
                withdraw_money(name, pin, amount)
            except ValueError:
                print("\n Amount must be number")
        elif choice=="4":
            transaction_history(name, pin)
        else:
            print("\n Invalid choice")

#direct calling
menu()