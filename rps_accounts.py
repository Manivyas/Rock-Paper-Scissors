print("-------------------------")
print("Rock, Paper, Scissor Account Setup")
print("-------------------------")

while True:
    username = input("Create Username: ")
    password = input("Create Password: ")
    password_confirm = input("Confirm your password: ")

    if password != password_confirm:
        print("Passwords didn't match!. PLease try again")

    if password == password_confirm:
        print("Your account has been setup.")
        text_file = open("accounts.txt", "a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break