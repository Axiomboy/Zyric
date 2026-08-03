write = print

USER_INPUT = input("hello. this version only uses write(). You can start coding.") 

if USER_INPUT[ :6] == ' write' or 'write':
    print(USER_INPUT[7: ])
else:
    print("Invalid Function")
