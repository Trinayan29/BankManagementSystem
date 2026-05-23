class BankAccount():
    def __init__(self,name,acc_no,balance=1000):
        self.name=name
        self.__balance=balance
        self.acc_no=acc_no
    def deposit(self,amount):
        self.__balance+=amount
        print(f"₹{amount} deposited successfully!!!!")
        print(f"Final Balance : ₹{self.__balance}")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance!!!")
        else :
            self.__balance-=amount
            print(f"₹{amount} deposited successfully!!!!")
            print(f"Final Balance : ₹{self.__balance}")
    def statement(self):
        print(f"Account Holder : {self.name}")
        print(f'Accounts No. : {self.acc_no[2]}XXXXX')
        print(f"Current Balance : ₹{self.__balance}")

acc={}
count=0

while True :
    print("--------WELCOME--------")
    print("1.SignUp")
    print("2.SignIn")
    print("3.Exit")
    try:
        opt=int(input("Enter Your Option (1-3): "))
        if opt>3:
            raise ValueError
    except ValueError:
        print("Please Enter Options from 1 to 3")
    
    if opt==1:
        name=input("Enter Your Name : ")
        passw=input("Create your password : ")
        acc[name]=passw
        print("Accounts created successfully!!!!")
    elif opt==2:
        namel=input("Enter Accounts Holder's Name : ")
        passl=input("Enter Your Password : ")
        if namel in acc.keys() and passl in acc.values():
            print("Logged In Successfully!!!!")
            user=BankAccount(namel,passw)
            while True :
                print("-----Main Menu-----")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Mini-Statement")
                print("4.LogOut")
                try:
                    opt2=int(input("Enter your option (1-4) : "))
                    if opt2>4:
                        raise ValueError
                except ValueError:
                    print("Invalid Option")
                if opt2==1:
                    am=float(input("Enter Amount to Deposit : "))
                    user.deposit(am)
                elif opt2==2:
                    aw=float(input("Enter Amount to Withdraw : "))
                    user.withdraw(aw)
                elif opt2==3:
                    user.statement()
                elif opt2==4:
                    print("Logged Out Successfully!!!")
                    print("Thank you!!!")
                    break
        else :
            print("Access Denied !!!")
            count+=1
            if count==3:
                print("Maximum No. of attempts reached!!!")
                exit()
    elif opt==3:
        print("Thank You!!!!")
        exit()
                    
