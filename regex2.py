def find_phone_number(text):
    import re 
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    if match:
        print(match.group(0))
    else:
        print('Pattern not found')

text = 'Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333'
find_phone_number(text)