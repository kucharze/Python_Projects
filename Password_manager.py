#Based off of a coding project in the following video: https://www.youtube.com/watch?v=NpmFbWO6HPU

pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = inpiut("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:#Open file for this section only for appending
        f.write(name + "|" + pwd + "\n")

mode = input(
    "Would you like to add an entry, view entries, or quit? (add/view/quit) ").lower()

if mode == "quit":
    quit()

elif mode == "view":
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line)

elif mode == "add":
    service = input("What service is the password for? ")
    password = input("What is the password? ")

    with open("passwords.txt", 'a') as f:
        f.write(service + ":" + password + "\n")


with open("passwords.txt", 'r') as f:
    for line in f.readlines():
        data = line.rstrip()
        service, password = data.split(":")
        print("Service: " + service + " | Password: " + password)