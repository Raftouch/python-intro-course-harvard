import re

email = input("What's your email? ").strip()

if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(com|edu|org|io)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")


# re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")