def find_phone_number(text):
    import re 
    pattern = r'\(?(\d{3})\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    match = re.search(pattern, text)
    if match:
        print(match.group(0))
    else:
        print('Pattern not found')

text = 'Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333'
find_phone_number(text)