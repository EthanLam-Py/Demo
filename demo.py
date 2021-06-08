origin_list = [1,2,3,4,5,6,7,8,9,10, 'a', 'b', 'c']
print('origin_list = ', origin_list)

origin_list.reverse()
print('reverse_list = ', origin_list)

number_list = []
char_list = []
for item in origin_list:
    if str(item).isdecimal():
            number_list.append(item)
    else:
        char_list.append(item)

print('number_list = ', number_list)
print('char_list = ', char_list)

print('print from Borsh')

print('print test SSH')