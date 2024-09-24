# Existing list of usernames
usernames = ['ancy', 'kiara', 'sujay', 'sowmya']

# Take input from the user
new_user = input("Please enter a new username: ").strip().lower()

# Check if the username is already in the list
if new_user in usernames:
    print("Username already present. Exiting.")
else:
    # Append the new user to the list
    usernames.append(new_user)
    print(f"Username '{new_user}' has been added to the list.")
    
# Optional: Print the updated list
print("Updated list of usernames:", usernames)
