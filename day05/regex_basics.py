import re
text= "Student ID:12345, Year:2026"
numbers=re.findall(r'\d+',text)
print("Extracted Numbers:",numbers)