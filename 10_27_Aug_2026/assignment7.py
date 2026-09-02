import re

text = input("Enter some text: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

emails = re.findall(pattern, text)

if len(emails) > 0:
    print("Emails found:")
    for email in emails:
        print(email)
else:
    print("No email found")