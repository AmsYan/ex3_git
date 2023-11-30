import random


def create_account():
    account_id = random.randint(0, 999)
    balance = random.randint(0, 99999)
    return (account_id, balance)


def balance_inquiry(client):
    return client[1]


def deposit(d, amount):
    pass


def withdraw(w, amount):
    pass


def account_summary(account_id):
    pass


person1 = create_account()
print(balance_inquiry(person1))
