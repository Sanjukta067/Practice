import re

text = "This is a Java program"
pattern = r"Java"
replacement = "Python"

result = re.sub(pattern, replacement, text)
print (result)
