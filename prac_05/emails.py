def extract_name(email):
    # Extract the name from the email by splitting at '@' and taking the first part
    email_split = email.split('@')[0]
    name_split = email_split.split('.')
    return ' '.join(name_split)


def main():
    email_to_name = {}
    is_true = True

    while is_true:
        email = input("Email: ").strip()

        if not email:
            is_true = False

        name = extract_name(email)
        name_input = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if name_input in ['n', 'no']:
            name = input("Name: ").strip().title()

        email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
