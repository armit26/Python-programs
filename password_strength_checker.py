password = input("Enter your Password :- ")

x = len(password)

has_upper = False
has_lower = False
has_number = False
has_special = False

if x < 8:
    print("Password is too small")

else:
    for ch in password:

        if ch.isupper():
            has_upper = True

        if ch.islower():
            has_lower = True
        
        if ch.isdigit():
            has_number = True

        if not ch.isalnum():
            has_special = True

    print("Uppercase present =", has_upper)
    print("Lowercase present =", has_lower)
    print("Number present =", has_number)
    print("Special character present =", has_special)

    if has_upper and has_lower and has_number and has_special:
        print("Password Strength = Strong")

    elif (has_upper or has_lower) and has_number:
        print("Password Strength = Medium")

    else:
        print("Password Strength = Weak")