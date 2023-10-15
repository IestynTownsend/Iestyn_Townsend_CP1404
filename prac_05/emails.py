def extract_name(email):
    # Extract the name from the email by splitting at '@' and taking the first part
    return email.split('@')[0].title()


def main():
    user_info = {}

    while True:
        email = input("Email: ").strip()

        if not email:
            break

        name = extract_name(email)
        name_input = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if name_input in ['n', 'no']:
            name = input("Name: ").strip().title()

        user_info[email] = name

    for email, name in user_info.items():
        print(f"{name} ({email})")


main()
