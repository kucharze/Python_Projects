logs = [
    {"input": "Hello", "response": "Hi there!"},
    {"input": "What’s your name?"},
    {"response": "I'm an AI."},
    {"input": "Bye", "response": "Goodbye!"}
]

for log in logs:
    print(log)

    if "input" in log and "response" in log:
        print("Valid log")
    else:
        print("Invalid log")
        del log


print(logs)