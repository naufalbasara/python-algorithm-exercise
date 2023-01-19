class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append(
            {
                'amount' : float(amount),
                'description' : description
            }
        )
        return

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    'amount': float(-amount),
                    'description': description
                }
            )
            return True
        return False

    def get_balance(self):
        self.total = 0
        for transaction in self.ledger:
            self.total += transaction['amount']
        return self.total

    def transfer(self, amount, object):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    'amount': float(-amount),
                    'description': f'Transfer to {object.category}'
                }
            )

            object.ledger.append(
                {
                    'amount': float(amount),
                    'description': f'Transfer from {self.category}'
                }
            )
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True
    
    def __repr__(self):
        output = f'{self.category}'.center(30, '*') + '\n'
        for transaction in self.ledger:
            #strip or cut string to fit in if length more than 30
            if(len(str(transaction['description'])) > 23) or (len(str(transaction['amount'])) > 7):
                output += str(transaction['description'])[:23].ljust(30-len(str(transaction['amount'])))
                output += str(transaction['amount'])[:7]
                output += '\n'
                continue
        
            output += str(transaction['description']).ljust(30-len(str(transaction['amount'])))
            output += str(transaction['amount'])
            output += '\n'

        output += f'Total: {self.get_balance()}'

        return output


def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    total_expenses = 0
    category_expenses = {}

    for category in categories:
        expense = 0
        for transaction in category.ledger:
            total_expenses += float(transaction['amount']) if transaction['amount'] < 0 else 0
            expense += float(transaction['amount']) if transaction['amount'] < 0 else 0
        category_expenses[f'{category.category}'] = expense
        expense = 0

    for i in range(100, -1, -10):
        output += f'{i}|\n'.rjust(5)

    return output