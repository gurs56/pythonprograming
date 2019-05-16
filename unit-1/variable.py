
#note- use == when you want to test for equal
#note- use != when you want to say not equal

def main():
    first_name = "Gursahaj"
    last_name = "Grewal"
    full_name = first_name + " " + last_name

    print(full_name)

    #boolean-variable - is ether true of false can not be anything else
    has_child = True

    #null/none- variable - has no value. 
    cars = None


def conditionals():
    # given a range of grade of 0 -100
    #if grade is between 80 and 100 - print "A"
    #if grade is between 60 and 79 - print "B"
    #if grade is between 50 and 59 - print "C"
    #0 - 40 - print "F"


    val = 25
    if val > 35:
        print("High")
    elif val > 15:
        print("medium")
    else:
        print("low")

    grade = 65
    if grade >= 80:
        print("A")
    elif grade >= 60:
        print("B")
    elif grade >= 50:
        print("C")
    else:
        print("F")

def fizzbuzz():
    """
    for the muber 1 to 50
    print "fizz" if the number is a multipe of 3
    print "buzz" if the number is a multiple of 5
    print "fizzbuzz" if the number is a multiple of 15
    otherwise print the number
    """

    for num in range(1, 51):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print ("fizz")
        else:
            print(num)


if __name__ == "__main__":
    fizzbuzz()