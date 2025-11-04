class Banking:
    def __init__(self, name, bank_name, pin ):
        self.name = name
        self.bank_name = bank_name
        self.__pin = pin
        self.balance = 0
        self.amount = 0
    @property
    def pin(self):
        return self.__pin
    
    def money_deposit(self):
        print(" Deposit Money")
        print("Enter your pin to deposit money:")
        pin_inp = input()
        if pin_inp != self.pin:
            print(" Incorrect pin entered. Access denied.")
            return False
        else:
            print(" Pin verified. You can now deposit money.")
            return True
    @property
    def money(self):
        print("Enter your amount to be deposited:")
        balance = int(input())
        if balance <= 0:
            print(" Invalid amount enterred for deposition .")
            return False
       
        else:
            self.balance += balance
            print(f" Money deposited to the bank of ₹{balance}. New balance: ₹{self.balance}")
            return True

    def get_balance(self):
        print(f" Current balance: ₹{self.balance}")
        return self.balance
    @property
    def summary(self):
        print("Card Summary:")
        print(f"Holder Name   : {self.name}")
        print(f"Bank Name     : {self.bank_name}")
        print(f"Card Number   : **** **** **** {self.pin[-4:]}")
        print(f"Current Balance: ₹{self.balance}")
    
    @property
    def payment( self  ):
      
        print("Enter your pin to withdraw money:")
    
        pin_inp = input()
      
        if pin_inp != self.pin:
            print(" Incorrect pin entered. Access denied.")
            return False
        else:
            print(" Pin verified. You can now withdraw money.")
            

            print("Enter withdrawal amount (or -1 to exit):")
            amount = int(input())
        
            if amount == -1:
             print(" Exiting transaction loop.")
             return False
            elif amount <= 0:
             print(" INVALID AMOUNT.")
            elif amount > self.balance:
             print(" Withdrawal amount exceeds balance.")
            elif self.balance - amount <= 0.1 * self.balance: 
              print(" Warning: You are near your credit limit!")
              self.balance -= amount
              print(f"Withdrawal of ₹{amount} successful. New balance: ₹{self.balance}")
              print(" Transaction Successful")
            else:  
             self.balance -= amount
             print(f" Withdrawal of ₹{amount} successful. New balance: ₹{self.balance}")
             
             print(" Transaction Successful")
       

card = Banking("Ishan", "CodeBank", "4444 9999 6666")

while True:
    print("\n What would you like to do?")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. View Card Summary")
    print("5. View Pin")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        card.money_deposit()
        card.money
        
    elif choice == '2':
        card.payment
        
    elif choice == '3':
        card.get_balance() 
    elif choice == '4':
        card.summary
    elif choice == '5':
        pin_inp = input("Enter your pin to view: ")
        if pin_inp == card.pin:
            print(f"Your pin is: {card.pin}")
        else:
            print(" Incorrect pin entered. Access denied.")
        
    elif choice == '6':
        print(" Exiting. Thank you!")
        break
    else:
        print("❌ INVALID CHOICE. Please enter a number from 1 to 6.")



