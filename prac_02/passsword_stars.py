def main():
    minimum_length = 6
    password = get_user_password(minimum_length)
    print_censored_password(password)


def get_user_password(minimum_length):
    password = input(f"Please enter your password ensuring it is at least {minimum_length} characters long: ")
    while len(password) < minimum_length:
        print(f"Password is not at least {minimum_length} characters long")
        password = input(f"Please enter your password ensuring it is at least {minimum_length} characters long: ")
    return password


def print_censored_password(password):
    print('*' * len(password))


main()
