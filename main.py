class Admin:
    def __init__(self):
        self.admin_data = {'admin': {'Email': "", 'loan_feature_enabled': True}}

    def total_bank_balance(self):
        print(f"Total bank balance: ৳ {bank.money:.2f}")

    def total_loan_amount(self):
        print(f"Total loan amount granted: ৳ {abs(user.ttl_loan):.2f}")

    def loan_feature_control(self):
        if self.admin_data['admin']['loan_feature_enabled']:
            self.admin_data['admin']['loan_feature_enabled'] = False
            print("Loan feature is now turned off.")
        else:
            self.admin_data['admin']['loan_feature_enabled'] = True
            print("Loan feature is now turned on.")

    def create_account(self):
        admin_email = input("> Enter Admin Name: ")
        self.admin_data['admin']['Email'] = admin_email
        print(f"Account created for {admin_email}, a new employee for our bank.")

class User:
    def __init__(self):
        self.user_data = {}
        self.ttl_loan = 0.0

    def create_account(self):
        user_email = input("> Enter your Email: ")
        initial_balance = 0
        self.user_data[user_email] = {'balance': initial_balance, 'transactions': []}
        print(f"~~~ Account created for {user_email} successfully ~~~")

    def check_balance(self):
        user_email = input("> Enter your Email: ")
        if user_email in self.user_data:
            print(f"~~~ Your current balance is: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
        else:
            print("~~~ User not found. ~~~")

    def deposit_money(self):
        user_email = input("> Enter your Email: ")
        if user_email in self.user_data:
            amount = float(input("> Enter the amount to deposit: "))
            if amount < 0:
                print("!!! Please enter a non-negative amount.")
                return
            self.user_data[user_email]['balance'] += amount
            bank.money += amount
            self.user_data[user_email]['transactions'].append(f"Deposited ৳ {amount:.2f}")
            print(f"~~~ ৳ {amount:.2f} deposited successfully. Current balance: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
        else:
            print("~~~ User not found. ~~~")

    def withdraw_money(self):
        user_email = input("> Enter your Email: ")
        if user_email in self.user_data:
            amount = float(input("> Enter the amount to withdraw: "))
            if amount < 0:
                print("!!! Please enter a non-negative amount.")
                return
            if amount <= self.user_data[user_email]['balance']:
                self.user_data[user_email]['balance'] -= amount
                bank.money -= amount
                self.user_data[user_email]['transactions'].append(f"Withdrew ৳{amount:.2f}")
                print(f"৳{amount:.2f} withdrawn successfully. Current balance: ৳{self.user_data[user_email]['balance']:.2f}")
            else:
                print("!!! Cannot withdraw due to insufficient balance.")
        else:
            print("~~~ User not found. ~~~")

    def transfer_money(self):
        sender_name = input("> Enter your Email: ")
        receiver_name = input("> Enter receiver's Email: ")
        if sender_name in self.user_data and receiver_name in self.user_data:
            amount = float(input(">> Enter the amount to transfer: "))
            if amount < 0:
                print("!!! Please enter a non-negative amount.")
                return
            if amount <= self.user_data[sender_name]['balance']:
                self.user_data[sender_name]['balance'] -= amount
                self.user_data[sender_name]['transactions'].append(f"Transferred ৳{amount:.2f} to {receiver_name}")
                self.user_data[receiver_name]['balance'] += amount
                self.user_data[receiver_name]['transactions'].append(f"Received ৳{amount:.2f} from {sender_name}")
                print(f"~~~ ৳{amount:.2f} transferred to {receiver_name} successfully. ~~~")
            else:
                print("!!! Cannot transfer due to insufficient balance.")
        else:
            print("~~~ User not found. ~~~")

    def transaction_history(self):
        user_email = input("Enter your Email: ")
        if user_email in self.user_data:
            print(f">>> Transaction history for {user_email}:")
            i = 1
            for transaction in self.user_data[user_email]['transactions']:
                print(i, ".", transaction)
                i += 1
        else:
            print("~~~ User not found. ~~~")

    def take_loan(self):
        if  (admin.loan_feature_control() == True):
            user_email = input("Enter your Email: ")
            loan_amount = float(input("Enter the amount of loan you want to take: "))
            if(loan_amount <= bank.money):
                if user_email in self.user_data:
                    if self.user_data[user_email]['balance'] > 0:
                        if loan_amount <= (self.user_data[user_email]['balance'] * 2):
                            self.ttl_loan += loan_amount
                            self.user_data[user_email]['balance'] += loan_amount
                            bank.money -= loan_amount
                            self.user_data[user_email]['transactions'].append(f"Took a loan of ৳ {loan_amount:.2f}")
                            print(f"Loan of ৳ {loan_amount:.2f} granted. Current balance: ৳ {self.user_data[user_email]['balance']:.2f}")
                        else:
                            print("!!! You can't take a loan greater than twice your balance")
                    else:
                        print("!!! Insufficient bank balance to take a loan")
                else:
                    print("~~~ User not found. ~~~")
            else:
                print("The the bank is bankrupt.")
        else:
            print("!!! You can't take loan untill admin allows.")


class Bank:
    def __init__(self):
        self.money = 10000000000


def main():
    while True:
        print("\n******** Bank Management System ********")
        print("1. User Options")
        print("2. Admin Options")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n******** Bank Management System ********")
            print("**** User Options ****")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transfer Money")
            print("6. Transaction History")
            print("7. Take Loan")
            print("8. Go Back")
            uo_c = input("Enter: ")
            if uo_c == "1":
                user.create_account()
            elif uo_c == "2":
                user.deposit_money()
            elif uo_c == "3":
                user.withdraw_money()
            elif uo_c == "4":
                user.check_balance()
            elif uo_c == "5":
                user.transfer_money()
            elif uo_c == "6":
                user.transaction_history()
            elif uo_c == "7":
                user.take_loan()
            elif uo_c == "8":
                continue
        elif choice == "2":
            print("\n******** Bank Management System ********")
            print("**** Admin Options ****")
            print("1. Create Account")
            print("2. Total Bank Balance")
            print("3. Total Loan Amount")
            if admin.admin_data['admin']['loan_feature_enabled']:
                print("4. Loan Feature on/off (currently on)")
            else:
                print("4. Loan Feature on/off (currently off)")
            print("5. Go Back")
            ad_c = input("Enter: ")
            if ad_c == "1":
                admin.create_account()
            elif ad_c == "2":
                admin.total_bank_balance()
            elif ad_c == "3":
                admin.total_loan_amount()
            elif ad_c == "4":
                admin.loan_feature_control()
            elif ad_c == "5":
                continue
        elif choice == "3":
            break

    print("\nThanks For Visiting")

if __name__ == "__main__":
    admin = Admin()
    user = User()
    bank = Bank()
    main()
