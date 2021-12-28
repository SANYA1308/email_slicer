# Get the user's email address
email=input('What is your email address? : ').strip()

# Slice out the user's email address

user_name = email[:email.index("@")]

# Slice out the domain

domain_name = email[email.index("@")+1 :]

# Display the result

result = "Your username is '{}' and your domain name is '{}' ".format(user_name,domain_name)

print(result)