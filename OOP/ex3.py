class Bank_Account:
    def __init__(self,owner,balance = 0):
        self.balance = int(balance)
        self.owner = owner
    def deposit(self,dep):
        print("Deposit Accepted")
        self.amount = int(dep)
        self.balance += self.amount
        print(f"Account Owner : {self.owner}"+"\n"+f"Account Balance : ${self.balance}")
    def withdrawal(self,withd):
        self.amount = int(withd)
        if self.balance<=self.amount:
            print("Withdrawal Declined")
            print("Reason : Fund Unavailable")
            print(f"Account Owner : {self.owner}"+"\n"+f"Account Balance : ${self.balance}")
        else:
            print("Withdrawal Accepted")
            self.balance-=self.amount
            print(f"Account Owner : {self.owner}"+"\n"+f"Account Balance : ${self.balance}")

            
        
        