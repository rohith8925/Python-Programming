#Store predefined username and password
correct_username = "admin"
correct_password = "password123"

# Get username and password from the user
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

# Check if the credentials are correct
if input_username == correct_username and input_password == correct_password:
    print(f"Welcome, {input_username}!🤝") #Correct credentials means print welcome along with username 
else:
    print("⚠️Invalid credentials.") # User enter wrong credentials means
