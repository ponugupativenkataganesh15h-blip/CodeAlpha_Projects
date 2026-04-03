import re

# Read file
with open("input.txt", "r") as file:
    data = file.read()

# Extract emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", data)

# Write to new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")
