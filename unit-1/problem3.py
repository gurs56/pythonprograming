my_string =  input("enter word or sentence")
my_new_string = []
reversed_string = ""

'''
for list in range(len(my_string)-1, -1, -1):
    

    print(my_string[list],end = '')
'''

#Strings are immutable. this means we can change strings

#or

for list in range(len(my_string)-1, -1, -1):
    reversed_string += my_string[list]

print(reversed_string)