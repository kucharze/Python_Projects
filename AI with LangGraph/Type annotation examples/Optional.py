from typing import Optional

def niceMessage(message: Optional[str]):
    if message is None:
        print("Hey random person!")
    else:
        print(f"Hi there, {message}!")

niceMessage(None)