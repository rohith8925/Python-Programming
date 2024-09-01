import os # To read system files

filename = input("Please enter the file name: ") # Get file name as a user input

if os.path.isfile(filename):
    print("File is present. Displaying the content:\n")    # Checking file is present or not . If present , display the content.
    with open(filename, 'r') as file:
        print(file.read())
else:
    print("File is not present.")

