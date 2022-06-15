import re

patterns = ["term1", "term2"]
text = "This is a string with term1, not the other"

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern, text):
        print("Match")
    else:
        print("No match")


split_term = "@"
email = "user@gmail.com"
print(re.split(split_term, email))

print(re.findall("match", "test phrase match in middle"))
