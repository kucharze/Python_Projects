#Based off of a coding project in the following video: https://www.youtube.com/watch?v=NpmFbWO6HPU

pwd = input("What is the master password? ")
with open("passwords.txt", 'r') as f:
    for line in f.readlines():
        data = line.rstrip()
        service, password = data.split(":")
        print("Service: " + service + " | Password: " + password)