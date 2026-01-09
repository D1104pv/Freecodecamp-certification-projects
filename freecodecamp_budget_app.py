class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []          
    
    # adding transaction to ledger list as a dictionary with amount and optional description
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    
    # first checking if withdraw is possible with chec
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description} )
            return True
        else:
            return False

    # returns balance
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance
    
    # calling check funds again to move money from one object to another
    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {Category.name}")
            Category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    # returns boolean value, comparing passed amount with balance
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    # printint formatted transactions and balance
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
    
# returns a string bar chart of percentage spending per category object
# takes list of Category objects as argument not a single object as argument 
def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    
    # calculating amount spent per category and maintaing a list for it (can also be done using a dictionary)
    spent_perc = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent_perc.append(total)
    
    # adding items of spent per category list for percentage spent calculation
    total_spent = sum(spent_perc)

    # calculating and rouding down the percentage to nearest 10
    percentage = []
    for i in spent_perc:
        percent = 0
        percent = int((i/total_spent * 100) // 10) * 10
        percentage.append(percent)
   
   # y - axis and bars
    graph = title
    for y in range(100, -1, -10):
        graph += f"{y:>3}|"
        for percent in percentage:
            if percent >= y:
                graph += " o "
            else:
                graph += "   "
        graph += " \n"

    # horizontal line
    graph += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # vertical category name
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        # adding the space to bring names in alignment with bars before printing names
        graph += "     "
        for category in categories:
            # adding each character horizontally name by name
            if i < len(category.name):
                graph += (category.name[i] + "  ") 
            else:
                graph += "   "
        graph += "\n"
    
    # removing the extra new line with strip
    return graph.rstrip("\n")
