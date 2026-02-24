import statistics as stat
from collections import Counter

class Statistics:
    def __init__(self, data=None):
        self.data = sorted(data) if data else []

    def add(self, value):
        self.data.append(value)
        self.data.sort()

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(stat.mean(self.data))

    def median(self):
        return stat.median(self.data)

    def mode(self):
        c = Counter(self.data)
        mode_val, cnt = c.most_common(1)[0]
        return {'mode': mode_val, 'count': cnt}

    def std(self):
        return round(stat.stdev(self.data), 1)

    def var(self):
        return round(stat.variance(self.data), 1)

    def freq_dist(self):
        c = Counter(self.data)
        total = self.count()
        return sorted([(round(v / total * 100, 1), k) for k, v in c.items()], reverse=True)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Variance: ', data.var())
print('Standard Deviation: ', data.std())
print('Frequency Distribution: ', data.freq_dist())

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income['income']
        return total
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense['expense']
        return total
    def account_info(self):
        return f'{self.firstname} {self.lastname}\n{self.incomes}\n{self.expenses}'
    def add_income(self, desc, income):
        self.incomes.append({"description": desc, "income": income})
        print("New income added!")
    def add_expense(self, desc, expense):
        self.expenses.append({"description": desc, "expense": expense})
        print("New expense added!")
    def account_balance(self):
        return self.total_income() - self.total_expense()

client = PersonAccount('Yurii', 'Kainskyi')
client.add_income("Salary", 500)
client.add_expense("Phone", 250)
client.add_income("Salary", 500)
client.add_expense("TV", 400)
client.add_income("Salary", 500)
client.add_expense("Microwave", 300)
client.add_income("Salary", 500)
client.add_expense("Transaction", 1000)
client.add_income("Salary", 500)
client.add_expense("Football", 50)
print(client.account_info())
print(client.account_balance())
print(client.total_income())
print(client.total_expense())