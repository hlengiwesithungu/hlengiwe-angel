# Declare the correct username and password
correct_username = "hlengiwe"
correct_password = "2004"

print("=== Login System ===")

# Allow the user 3 attempts
for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome.")
        break
    else:
        print("Incorrect username or password.")
        print(f"Attempts left: {2 - attempt}\n")

# If 3 attempts failed
if username != correct_username or password != correct_password:
    print("You have been locked out. Too many failed attempts.")
    