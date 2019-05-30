
def print_message():
    print("Hello world")

print_message()

#fuction with a single argument 
def print_message2(message):
    print(message)

print_message2("hey my guy")

#fuctions that returns a result
def sqaure(value):
    result = value * value
    return result

answer = sqaure(10)
print(answer)

print(sqaure(50))

#Fuction witj multiple argumnets
def greetings(name,job,hobby):
    print(f"hello{name} you job is {job} and you like {hobby}")

greetings("Gursahaj", "Pimp", "doing blow")



my_lsit = ["hello", "my", "guy"]

"""
def reverse_list(my_list):
    length = len(my_lsit)
    s = length

    for item in my_lsit:
        s = s
"""

def reverse_list(my_list):
    new_list = []
    #iterate over lsit in reverse order
    for index in range(len(my_list)- 1, -1, -1):
        #add each element to new lsit 
        new_list.append(my_list[index])
    #return the revered list 
    return new_list

thing = ["hello", "my", "guy"]

result = reverse_list(thing)

print(result)


    #check if word is the same forwards as backwards
    #return True if it is, false otherwise


"""
#this doesnt work

def reverse_string(my_string):
    reversed_string = ""
    for i in range(len(my_string)-1,-1,-1):
        reversed_string += my_string[i]
    return reverse_string

def is_pal(word):
    word_revered = reverse_string(word)
    if word_revered == word:
        return True
    return False
    #return true if it is, false otherwise

print(is_pal("level"))
"""

