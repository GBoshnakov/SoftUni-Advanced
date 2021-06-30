class MustContainAtSymbolError(Exception):
    pass


class MustContainOnlyOneAtSymbol(Exception):
    pass


class NameTooShort(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validator(email):
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain, *rest = email.split("@")

    if rest:
        raise MustContainOnlyOneAtSymbol("Email cannot contain more than one @ symbol")

    if len(username) <= 4:
        raise NameTooShort("Name must be more than 4 characters")

    if "." not in domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if domain.split(".")[-1] not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

# This is with shorted error message + 'end' command to stop the program
#
# def main():
#     email = input()
#     while email != "end":
#         try:
#             validator(email)
#         except (NameTooShort, MustContainOnlyOneAtSymbol, MustContainAtSymbolError, InvalidDomainError) as error:
#             print(error)
#         email = input()
#     print("Program ends here.")


def main():
    while True:
        email = input()
        validator(email)


main()


# WITHOUT FUNCTIONS
#
# email = input()
# while True:
#     if "@" not in email:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     username, domain, *rest = email.split("@")
#
#     if rest:
#         raise MustContainOnlyOneAtSymbol("Email cannot contain more than one @ symbol")
#
#     if len(username) <= 4:
#         raise NameTooShort("Name must be more than 4 characters")
#
#     if "." not in domain:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     if domain.split(".")[-1] not in ["com", "bg", "org", "net"]:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     print("Email is valid")
#     email = input()
