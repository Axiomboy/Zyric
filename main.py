
def write(text):
    print(text)

def user():
    return input("Enter your input: ")

print("Hello. Version 0.0.3 can only use write and input. You are able to code now.")

User_Input = None

while True:
    User_Code = input("Enter command: ").strip()

    if User_Code.startswith("echo"):
        command_text = User_Code[5:].strip()
        write(command_text)

    elif User_Code.startswith("user"):
        User_Input = user()
        write(f"User input: {User_Input}")

    elif User_Code[6:] == User_Input and User_Code.startswith("echo"):
        write(User_Input)

    
    
    




