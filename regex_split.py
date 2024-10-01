import re

text = "apple,banana,grape,jackfruit"
split_text= r","

split_result = re.split(split_text, text)

print (split_result[0])

