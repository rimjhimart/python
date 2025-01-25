#CREATING USERNAME 
#1. It must not contain more that 12 letters.
#2. It must not contain any spaces.
#3. It must not contain any digits.

username = input("write your username: ")
if len(username)>12:
    print("username can not have more than 12 letters.")
elif not username.find(" ")==-1:
    print("your username can not have any spaces.")
elif not username.isalpha():
    print("your username can not have any digits.")
else:
    print(f"Welcome {username}")