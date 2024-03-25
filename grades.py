mark=int(input('Enter yor mark '))
if(mark<40):
    print('FAIL')
elif(mark>=40 and mark<49):
    print('D')
elif(mark>=50 and mark<59):
    print('C')
elif(mark>=60 and mark<69):
    print('B')
else:
    print('A')