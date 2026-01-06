f_name = input("Enter your first name: ").lower().strip()
l_name = input("Enter your last name: ").lower().strip()

existing_mails = {
    "kiran@gmail.com", 
    "saikiran@gmail.com", 
    "sai@gmail.com", 
    "kiran123@gmail.com", 
    "sai69@gmail.com"
}

print("Select your domain:")
print("1) Gmail")
print("2) Outlook")
print("3) Yahoo")
print("4) ProtonMail")

choice = input("Enter your choice (1-4): ")

# Domain Mapping
if choice == "1":
    domain = "gmail.com"
elif choice == "2":
    domain = "outlook.com"
elif choice == "3":
    domain = "yahoo.com"
elif choice == "4":
    domain = "protonmail.com"
else:
    print("Invalid choice, defaulting to Gmail.")
    domain = "gmail.com"

# creating username
user_name = f_name + l_name
email_id = user_name + "@" + domain
print("Your mail id is:", email_id)
