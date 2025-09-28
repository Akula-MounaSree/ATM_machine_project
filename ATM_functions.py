from predefined_acc import accounts
#FIND ACCOUNTS
def find_account(name, pin):   #use name or pin
    for account in accounts:
        if account["name"].lower()==name.lower() and account["pin"]==pin:
            return account
    return None

#CHECK BALANCE -- NAME, PIN
def check_balance(name, pin):
    account=find_account(name, pin)
    if account:
        print(f"\n Balance for {account['name']}: ₹{account['balance']}\n")
    else:
        print("\n Invalid name or pin")

#DEPOSIT MONEY   #use name,pin,amount to check balance
def deposit_money(name, pin, amount):
    account=find_account(name,pin)
    if account:
        if amount>0:   #amount must be >0
            account["balance"]+=amount  #balance+amt
            account["transactions"].append(f"Deposited ₹{amount}")  #transaction+deposited = new balance 
            print(f"\n Deposited ₹{amount}. New balance: ₹{account['balance']}\n")
        else:
            print("\n Deposit amount must be greater than 0.\n")
    else:
        print("\n Invalid name or pin\n") 

#wITHDRAW MONEY --- NAME, PIN, AMOUNT
def withdraw_money(name,pin, amount):
    account=find_account(name, pin)
    if account:
        if amount<=0: #can't withdraw the amt 
            print("\n Withdraw amount must be greater than 0.\n")
        elif account["balance"]>=amount:  #present balance 
            account["balance"]-=amount   #balance - withdraw amt
            account["transactions"].append(f"withdraw ₹{amount}")  #transaction+withdraw amt
            print(f"\n withdraw ₹{amount}. new balance: ₹{account['balance']}\n") #= produce new balance
        else:
            print("\n Insufficient Balance.")
    else:
        print("\n Invalid name or pin")

#TRANSACTION HISTORY -- NAME, PIN
def transaction_history(name, pin):
    account=find_account(name, pin)
    if account:
        print(f"\n Transaction History for {account['name']}:")
        if account["transactions"]:
            for t in account["transactions"]:
                print(f"-{t}")
        else:
            print("No transactions yet")
        print()
    else:
        print("\n Invalid name or pin")
