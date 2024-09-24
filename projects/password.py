import re
def check_password(password):

    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    
    if not re.search(r"[@$!%*?$#]", password):
        return "Password must contain at least one speacial character"
    
    return "Password is valid"

user_password = input("Enter your password:")
result = check_password(user_password)
print(result)