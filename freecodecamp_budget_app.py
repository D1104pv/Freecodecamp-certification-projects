class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []          
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description} )
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance
    
    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {Category.name}")
            Category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, "*")
        
        feild = ""
        cost = ""
        entries = ""
        for item in self.ledger:
            feild = item["description"][:23]
            cost = item["amount"]
            entries += "\n" + f"{feild:<23}{cost:>7.2f}"
        
        total = "\n" + f"Total: {self.get_balance()}" 

        return title + entries + total
    
def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spent_perc = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent_perc.append(total)
    
    total_spent = sum(spent_perc)
   
    percentage = []
    for i in spent_perc:
        percent = 0
        percent = int((i/total_spent * 100) // 10) * 10
        percentage.append(percent)
   
    graph = title
    for y in range(100, -1, -10):
        graph += f"{y:>3}|"
        for percent in percentage:
            if percent >= y:
                graph += " o "
            else:
                graph += "   "
        graph += " \n"

    graph += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        graph += "     "
        for category in categories:
            if i < len(category.name):
                graph += (category.name[i] + "  ") 
            else:
                graph += "   "
        graph += "\n"
    
    return graph.rstrip("\n")




food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(100.15, 'groceries')
food.withdraw(150.89, 'dessert')
food.withdraw(500, "protein")

clothing = Category("Clothing")
clothing.deposit(1000, "deposit")
clothing.withdraw(200, "shirt")
clothing.withdraw(150, "pants")
clothing.withdraw(500, "shoes")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(200, "fuel")
auto.withdraw(100, "service")
auto.withdraw(50, "air")

print(create_spend_chart([food, clothing, auto]))