import re

with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    text = input_file.read()
    email_pattern = r'\S+@\S+'

    emails = re.findall(email_pattern, text)

    output_file.write(", ".join(emails))
