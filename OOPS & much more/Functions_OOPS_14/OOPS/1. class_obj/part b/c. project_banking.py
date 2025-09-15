from random import randint


class Bank:
    def __init__(self):
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name = ")
        self.ph_num = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Full name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    def show_bal(self):
        print(f"Current balance = {self.balance}")

    def withdraw(self):
        amt = int(input("Enter amount to withdraw = "))
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amt

    def deposit(self):
        amt = int(input("Enter amount to deposit = "))
        self.balance += amt


Banks = []


def check_account_exist(acc_no: int):
    global Banks
    for obj in Banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. Create account")
    print("2. Show all bank details.")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Exit")
    choice = int(input("Enter choice = "))
    if choice == 1:
        obj = Bank()
        Banks.append(obj)
    elif choice == 2:
        if len(Banks) == 0:
            print("No accounts have been created yet.")
        else:
            for acc in Banks:
                acc.show_info()
    elif choice == 3:
        if len(Banks) == 0:
            print("No accounts have been created yet.")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in Banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
    elif choice == 4:
        if len(Banks) == 0:
            print("No accounts have been created yet.")
        else:
            acc_no = int(input("Enter account number to withdraw = "))
            for obj in Banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        from_acc_no = int(
            input("Enter account number from which you want to transfer =  ")
        )
        to_acc_no = int(input("Enter account number to which you want to transfer =  "))
        from_acc_obj = check_account_exist(from_acc_no)
        to_acc_obj = check_account_exist(to_acc_no)
        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient balance.")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("Acoount does not exist.")
    elif choice == 6:
        break
    else:
        print("Invalid Input")
