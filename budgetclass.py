from pathlib import Path

class Budget:

    def __init__(self, name):
        self.name = name
        self.path = Path.cwd()
        self.__readBalance()
        
    def __readBalance(self):
        p = self.path / 'budgetfiles' / (self.name + '.txt')
        if p.exists():
            with p.open('r') as f:
                self.balance = float(f.read())
        else:
            self.balance = 0.0

    def __writeBalance(self):
        folder = self.path / 'budgetfiles'
        if not folder.exists():
            folder.mkdir()

        p = folder / (self.name + '.txt')
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

#    def summary():





    
