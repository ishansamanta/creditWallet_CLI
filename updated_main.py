class Banking:
    def __init__(self, name, bank_name, pin ):
        self.name = name
        self.bank_name = bank_name
        self.pin = pin
        self.balance = 0
        self.amount = 0

    def money_deposit(self):
        print("Enter your amount to be deposited:")
        balance = int(input())
        if balance <= 0:
            print("❌ Invalid amount enterred for deposition .")
            return False
       
        else:
            self.balance += balance
            print(f"✅ Money deposited to the bank of ₹{balance}. New balance: ₹{self.balance}")
            return True

    def get_balance(self):
        print(f"💰 Current balance: ₹{self.balance}")
        return self.balance
    
    def get_summary(self):
        print("Card Summary:")
        print(f"Holder Name   : {self.name}")
        print(f"Bank Name     : {self.bank_name}")
        print(f"Card Number   : **** **** **** {self.pin[-4:]}")
        print(f"Current Balance: ₹{self.balance}")
   
    def make_payment( self  ):
      while True:
        print("Enter payment amount (or -1 to exit):")
        amount = int(input())
        
        if amount == -1:
            print("🔁 Exiting payment loop.")
            break
        elif amount <= 0:
            print("❌ INVALID AMOUNT.")
        elif amount > self.balance:
            print("❌ Payment exceeds balance.")
        elif self.balance - amount <= 0.1 * self.balance: 
            print("⚠️ Warning: You are near your credit limit!")
            self.balance -= amount
            print(f"✅ Payment of ₹{amount} received. New balance: ₹{self.balance}")
            print("💸Transaction Successful")
        else:  
            self.balance -= amount
            print(f"✅ Payment of ₹{amount} received. New balance: ₹{self.balance}")
            print("💸Transaction Successful")
           
           
    
    

card = Banking("Ishan", "CodeBank", "4444 9999 6666")

while True:
    print("\n What would you like to do?")
    print("1. Deposit Money")
    print("2. Make a Payment")
    print("3. View Balance")
    print("4. View Card Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        card.money_deposit()
        
    elif choice == '2':
        card.make_payment()
        
    elif choice == '3':
        card.get_balance()
    elif choice == '4':
        card.get_summary()
    elif choice == '5':
        print("👋 Exiting. Thank you!")
        break
    else:
        print("❌ INVALID CHOICE. Please enter a number from 1 to 5.")



