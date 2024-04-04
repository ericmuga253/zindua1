'''
user_input=int(input('what is your range? '))
for number in range(user_input):
    if(number%3==0):
        print(f'{number} this is a multiple of 3')
        '''
user_input=[1,2,3,4,5,6,7,8,9]
for item in (user_input):
    if (item%1==0 and item%item==0):
        print(item)