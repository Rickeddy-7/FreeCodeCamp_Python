
class Category:
    
    def __init__(self,category):
        self.name = category
        self.ledger = []
        self.acc_bal = 0

    def __str__(self):
        """represents the object in a receipt-like, string format"""

        image = []
        # image.append(self.name.center(30,'*'))
        image.append(f'{self.name:*^30}')

        for transaction in self.ledger:
            detail = transaction['description'][:23] # only print the first 23 chars if len > 23
            amount = f"{transaction['amount']:.2f}" # convert amount to a number rounded to two decimal places
            space = ' ' * (30 - (len(detail) + len(amount)))
            image.append(detail + space + amount) # entire formatted transaction
        image.append(f'Total: {self.acc_bal}')

        return '\n'.join(image)

    def deposit(self,amount,description=''):
        """adds transactions to the ledger"""

        deposit = {'amount': amount,'description': description}
        self.ledger.append(deposit)
        self.acc_bal += amount

    def withdraw(self,amount,description=''):
        """subtracts funds from the account and adds to the ledger"""

        can_withdraw = self.check_funds(amount)
        if not can_withdraw: return False

        withdrawal = {'amount': -amount,'description': description}
        self.ledger.append(withdrawal)
        self.acc_bal -= amount
        return True

    def get_balance(self):
        """returns the current account balance for the category"""

        return self.acc_bal
    
    def check_funds(self,n):
        """returns true if n <= account balance"""

        if n > self.acc_bal: return False
        return True

    def transfer(self,n,cat):
        """transfers funds to another category(cat) if funds(n) are
           available and returns false if the transfer failed"""

        can_transfer = self.check_funds(n)
        if not can_transfer: return False

        self.withdraw(n,f'Transfer to {cat.name}')
        cat.deposit(n,f'Transfer from {self.name}')
        return True


def create_spend_chart(categories):
    """returns a bar graph from the list of categories"""

    expenses = total_spending(categories)
    total = sum(expenses)
    percentages = list(map(lambda x: round((x/total)*100),expenses))

    # Create the bar chart substrings
    chart = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        chart += f'{i:>3}|'
        for p in percentages:
            if p >= i: chart += ' o '
            else: chart += '   '
        chart += ' \n'

    chart += "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    
    names = [cat.name for cat in categories]
    max_len = max([len(name) for name in names])
    # format category names and print them vertivally:
    names = [extend(name,max_len) for name in names]
    for i in range(max_len):
        chart += '    '
        for name in names:
            chart += f' {name[i]} '
        if i != max_len-1:
            chart += ' \n'
        else: chart += ' '
    
    return chart


def extend(word,n):
    """adds empty spaces to word to make it length n"""

    while len(word) != n:
        word += ' '
    return word


def total_spending(categories):
    """returns a list of the total expenditure in each category"""

    expenses = []
    for cat in categories:
        expenditure = []
        for trans in cat.ledger:
            if trans['amount'] < 0: expenditure.append(trans['amount'])
        expenses.append(sum(expenditure))
    
    return expenses


# print("{}".format(self.name).center(30, "*"))
# for item in self.ledger:
#     print("{}".format(item["description"][:23]) + " {:.2f}".format(item["amount"]).rjust(30 - len(item["description"])))
# print("Total: {:.2f}".format(self.get_balance()))
# return ""