playlist = [{"title": "bodak yellow", "artiste": "Cardi B", "year": "2017", "genre": "pop", "length": 3.25},
{"title": "earfquake", "artiste": "Tyler, The Creator", "year": "2019", "genre": "hip-hop", "length": 3.10},
{"title": "somthing about him", "artiste": "brockhamton", "year": "2018", "genre": "hip-hop", "length": 1.22},
{"title": "song 2", "artiste": "blur", "year": "2000", "genre": "rock", "length": 2.01},
{"title": "still here", "artiste": "drake", "year": "2016", "genre": "pop", "length": 3.09},
{"title": "wyclef jean", "artiste": "young thug", "year": "2016", "genre": "rap", "length": 3.56},
{"title": "weekend", "artiste": "mac miller, miguel", "year": "2015", "genre": "hip-hop", "length": 3.28},
{"title": "timmy turner", "artiste": "desiinger", "year": "2016", "genre": "rap", "length": 3.59},
{"title": "all day", "artiste": "kanye west", "year": "2016", "genre": "hip-hop", "length": 5.10},
{"title": "back in black", "artiste": "ac/dc", "year": "1980", "genre": "rock", "length": 4.15}]

#print(playlist)
pop_playlist = {}

def display_titles(my_list):
    for song in my_list:
        print(song["title"])


def display_artistes(my_list):
    for song in my_list:
        print(song["artiste"])

def get_playlength(my_list):
    play_length = 0
    for song in my_list:
        play_length += song["length"]

    return play_length

def get_mostpop(my_list):
    for song in pop_playlist:
        if song in my_list:
            pop_playlist[my_list] += 1
        else:
            pop_playlist[my_list] = 1
    print(pop_playlist)


def print_menu():
    print("1. Display song titles")
    print("2. Display song artistes")
    print("3. Display song length")
    print("4. Display most popular genre")

print_menu()
choice = int(input("Enter your choice[5 to end] "))
while(choice != 5):
    if choice == 1:
        display_titles(playlist)
    elif choice == 2:
        display_artistes(playlist)
    elif choice == 3:
        print ("print length is {}".format(get_playlength(playlist)))
    elif choice == 4:
        print(get_mostpop)


    choice = int(input("Enter your choice[5 to end]"))
