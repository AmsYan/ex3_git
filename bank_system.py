import random


def create_account():
    """    Create a new bank account with a randomly generated account ID and balance.
    :return list representing them
"""
    account_id = random.randint(0, 999)
    balance = random.randint(0, 99999)
    return [account_id, balance]


def balance_inquiry(client):
    """ receive client info and return the balance amount"""
    return client[1]


def deposit(client, amount):
    """receive client info and amunt to add return new balance"""
    client[1] = client[1] + amount
    return client[1]


def withdraw(client, amount):
    """receive client info and amount to withdraw check if thre is enough money
    if yes return new balance"""
    if client[1] >= amount:
        client[1] = client[1] - amount
        return client[1]
    else:
        print("there is no enough money")
        return


def account_summary(client):
    """ receive client info and return a summary of the info"""
    print(f"The client {client[0]} have a balance of {client[1]}")


person1 = create_account()
print(balance_inquiry(person1))
person1[1] = deposit(person1, 1000)
print(balance_inquiry(person1))
withdraw(person1, 10000)
print(balance_inquiry(person1))
account_summary(person1)
