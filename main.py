write = print

User_Code = input("Hello. Version 0.0.1 can only use write(). You are able to code now ")

if User_Code[0:6] == " write":
    write(User_Code [7:])
else:
    write("Nonexistent Function")

