class Atm:
    def __init__(self,cardNumber,pin):
        self.pin = pin
        self.cardNumber = cardNumber
        self.balance = 0
    
    def checkBalance(self):
        print(f"You acount balance is ${self.balance}")

    def widrawMoney(self,amount):
        self.balance -= amount
        print(f"You have sucsessfully widrawn ${amount}")

    def depositMoney(self,amount):
        self.balance += amount
        print(f"You have sucsessfully deposited ${amount}")
    
myatm = Atm(999,999)
print(myatm.checkBalance())

myatm.depositMoney(100)

myatm.widrawMoney(50)

myatm.checkBalance()