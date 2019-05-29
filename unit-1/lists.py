#declara an empty list
classmates = []

#add items to list 
classmates.append("Sue")
classmates.append("Shad")
classmates.append("Gus")
classmates.append("Chin")
classmates.append("Eva")
classmates.append("Jeremy")
classmates.append("Dan")
classmates.append("Julian")
classmates.append("Aaron")

'''
#access an item at specific postion
print(classmates[0])

print(classmates[5])#fifth element

#get the size of list
print(len(classmates))

#remove an item from end of list 
classmates.pop()

print(classmates)

#insert at specific postion
classmates.insert(0,"Aaron")

print(classmates)

#removing an item form the list 
classmates.remove("Gus")

print(classmates)

#edit an item in the list 
classmates[1] = "Sue Work"

print(classmates)

'''
'''
#iterate over list
for classmate in classmates:
    if(classmate == "Gus"):
        print("Great, Im in the class!")
'''
'''
#edit element while iterating 
for index, classmate in enumerate(classmates):
    classmates[index] += "- Python Student"

print(classmates)
'''
'''
for index, classmate in enumerate(classmates):
    #classmates[index] = classmates[index].upper()
    classmates[index] = classmate.upper()


print(classmates)
'''
#create a list all the marvel movies 
#Go thru, and create a second list with all the  title that have "the"
#in their names

'''
marvel_movie =["Iron man", "The Increble Hulk", "Iron man 2", "Thor", "Caption American the First Avenger", "The Avenger", "Iron man 3","Caption American The Winter Solder", "Thor The Dark World", "The Gurdians of The galaxy", "Avenger Age of Ultron","Antman" ]
the_marvel_movie = []

#print(marvel_movie)

for index, movie in enumerate(marvel_movie):
    #marvel_movie[index] = marvel_movie[index].upper()
    if "the " in movie.lower():
    #if "the " in marvel_movie[index]: this is wrong

        the_marvel_movie.append(movie)
        #print(movie)
        
print(the_marvel_movie)
print(len(marvel_movie))
'''
marvel_movie =["Iron man", "The Increble Hulk", "Iron man 2", "Thor", "Caption American the First Avenger", "The Avenger", "Iron man 3","Caption American The Winter Solder", "Thor The Dark World", "The Gurdians of The galaxy", "Avenger Age of Ultron","Antman" ]

the_marvel_movie = []

'''
for movie in marvel_movie:
        if "the" in movie.lower():
                the_marvel_movie.append(movie)

print(the_marvel_movie)
'''
'''
#get index of list
for index in range(len(marvel_movie)):
        print(index)
'''