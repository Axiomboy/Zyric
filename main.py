write = print
User_Code = input("Hello. This version 0.0.1 can only use the write function. Start coding")
if User_Code[0:6] == " write":
    write(User_Code [7:])
else:
    write("Nonexistent Function")

