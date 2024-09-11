from validator_collection import validators, checkers, errors

if email_address := checkers.is_email(input("Enter your email: ")):
    print("Valid")
else:
    print("Invalid")




