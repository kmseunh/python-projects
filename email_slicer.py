def email_slicer(email_input):
    try:
        username, domain = email_input.split("@")
        domain, extension = domain.split(".")
        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)
    except ValueError:
        print("Invalid email address format!")


def main():
    print("Welcome to the email slicer")
    print("")

    while True:
        email_input = input("Input your email address (or 'q' to quit): ")
        if email_input.lower() == "q":
            print("Program ended.")
            break
        email_slicer(email_input)


if __name__ == "__main__":
    main()
