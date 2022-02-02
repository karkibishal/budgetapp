from pathlib import Path

class Budget:

    def __init__(self, name):
        self.name = name
        self.__readBalance()
        
    def __readBalance(self):
        p = Path(self.name + '.txt')
        if p.exists():
            with open(p, 'r') as f:
                self.balance = float(f.read())
        else:
            self.balance = 0.0

    def __writeBalance(self):
        p = Path(self.name + '.txt')
        with open(p, 'w') as f:
            f.write(str(self.balance))
    
    def deposit(self, amount):
        self.balance += amount
        self.__writeBalance()

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!!!")
        else:
            self.balance -= amount
            self.__writeBalance()



    
