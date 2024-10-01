import re

text = "pyhton java c c++ django ansible shell-script"
pattern = r"ansible"

search = re.search(pattern,text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")