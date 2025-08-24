import random

def generate_random_email():
    f_name = ["dave", "John", "Paul", "Steve", "Joe"]
    l_name = ["Doe", "Smith", "Jones", "Peters"]

    rand_num = random.randint(20,99)
    x = random.choice(f_name)
    y = random.choice(l_name)
    rand_email = f"{x}{y}{rand_num}@mydomain.com"
    print(rand_email)
    another_email()

def another_email():
    print("Print more?")
    entry = input("Y or N ")
    if entry.lower()== "y":
        generate_random_email()
    else:
        quit()

generate_random_email()