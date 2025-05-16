#Based off of a coding project in the following video: https://www.youtube.com/watch?v=NpmFbWO6HPU


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()#Rstrip is to remove the \n
            user, passw = data.split("|")#split the data into array
            print("User: ", user, ", Password: ", passw)
            

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:#Open file for this section only for appending
        f.write(name + "|" + pwd + "\n")


pwd = input("What is the master password? ")


mode = input(
    "Would you like to add an entry, view entries, or quit? (add/view/quit) ").lower()

if mode == "quit":
    quit()

elif mode == "view":
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line)

elif mode == "add":
    add()