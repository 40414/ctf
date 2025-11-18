import re

filename = "misc100"
with open(filename, "r", encoding="shift_jis") as ifile:
    data = ifile.read()

print(re.sub("[a-z, !]", "", data))
