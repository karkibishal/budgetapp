from pathlib import Path
folderpath = Path.cwd() / 'budgetfiles'

class Budget:

    def __init__(self, name):
        self.name = name
        self.__readBalance()
        
    def __readBalance(self):
        p = folderpath / (self.name + '.txt')
        if p.exists():
            with p.open('r') as f:
                self.balance = float(f.read())
        else:
            self.balance = 0.0

    def __writeBalance(self):
        if not folderpath.exists():
            folderpath.mkdir()

        p = folderpath / (self.name + '.txt')
        with p.open('w') as f:
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

    def summary():
        for file in folderpath.iterdir():
            print(file.stem + ':')
            with file.open('r') as f:
                print(f.read() + '\n')
