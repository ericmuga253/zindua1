import re
def find_phone_number(text):
   
    pattern = r'\(?(\d{3})\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    match = re.search(pattern, text)
    if match:
        print(match.group(0))
    else:
        print('Pattern not found')

text = 'Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333'
find_phone_number(text)
def find_email(text):
   
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    if match:
        print(match.group(0))
    else:
        print('Pattern not found')

text = 'Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333'
find_email(text)

def replace_email_addresses(string, replacement):
    pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
    
    replaced_string =  re.sub(pattern, replacement, string)

    print (replaced_string)

replace_email_addresses('Please contact info@example.com for assistance.', 'REPLACEMENT')