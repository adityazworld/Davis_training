def login():

    correct_username = "Admin"
    correct_password = "1234"
    max_attempts = 3

    attempts = 0
    print("=" * 35)
    print("WelCome to Login System")
    print("=" * 35)

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nAttempt {attempts + 1} of {max_attempts}  ({remaining} remaining)")
        ## enter username and password
        username = input ("Enter Username: ")
        password = input ("Enter Password: ")

        if username == correct_username and password == correct_password :
            print("\n" + "=" * 35)
            print("      ✅ Login Successful!")
            print(f"      Welcome, {username}!")
            print("=" * 35)

            return

        else:
         attempts +=1
        if attempts < max_attempts :
         print("Incurrect Password")

login()
