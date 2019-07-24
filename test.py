"""
#globe scope
num = 10
def change_num(num):
    #function scope
    num += 5
    print("inside function num is {}".format(num))

#intergers are passed by value, i.e we pass a copy to functions
change_num(num)

print("out{}".format(num))

nums = [1,2,3,4,5]

def change_nums(vals):
    for index in range(len(vals) - 1):
        vals[index] += 5
    print("inside the funtion {}".format(vals))

#lists are pass by-reference
change_nums(nums)

print("outside the function")
"""
scores = [5,15,25,4,6,7,3,45,67,78,78,7,5,15,6,6,6]

frequency_conunter = {} #This is an empty dictionary 

for score in scores:
    if score in frequency_conunter:
        frequency_conunter[score] += 1
    else:
        frequency_conunter[score] = 1

print(frequency_conunter)