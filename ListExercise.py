# Task 1
names = ["Usama", "Gufran", "Rizwan", "Sameer", "Umer"]

for name in names:
    print(name)

# Task 2
names = ["Usama", "Gufran", "Rizwan", "Sameer", "Umer"]

for name in names:
    print(f"Your name is {name}, and you are not a terrorist.")

# Task 3
transportation_modes = ["Car", "PrivateJet", "Yacht"]

for mode in transportation_modes:
    print(f"I would like to own a {mode}.")

# Task 4
guest_list = ["Wasim Akram", "Shahid Afridi", "Babar Azam"]

for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner at my place. Looking forward to your presence!")

# Task 5
guest_list = ["Wasim Akram", "Shahid Afridi", "Babar Azam"]

for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner at my place. Looking forward to your presence!")

print("\nUnfortunately, Shahid Afridi can't make it to the dinner.\n")

guest_list[1] = "Shoaib Akhtar"

for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner at my place. Looking forward to your presence!")

# Task 6
guest_list = ["Wasim Akram", "Shoaib Akhtar", "Babar Azam"]

print("Great news! We found a bigger table and can invite more guests.\n")

guest_list.insert(0, "Younis Khan")  
middle_index = len(guest_list) // 2
guest_list.insert(middle_index, "Misbah-ul-Haq")  
guest_list.append("Sarfaraz Ahmed")  

for guest in guest_list:
    print(f"Dear {guest}, you are cordially invited to dinner at my place. Looking forward to your presence!")

# Task 7
guest_list = ["Younis Khan", "Wasim Akram", "Misbah-ul-Haq", "Shoaib Akhtar", "Babar Azam", "Sarfaraz Ahmed"]

print("Unfortunately, we can only invite two people for dinner.\n")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, we can't invite you to dinner.")

for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner. Looking forward to your presence!")

del guest_list[:]

print("\nFinal guest list:", guest_list)

# Task 8
places = ["Switzerland", "Zell am See", "Hallstatt Skywalk", "Berchtesgaden", "Bali"]

print("Original list:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nList still in original order:")
print(places)

print("\nReverse-alphabetical order:")
print(sorted(places, reverse=True))

print("\nList still in original order:")
print(places)

places.reverse()
print("\nList after reversing:")
print(places)

places.reverse()
print("\nList restored to original order:")
print(places)

places.sort()
print("\nList sorted in alphabetical order:")
print(places)

places.sort(reverse=True)
print("\nList sorted in reverse-alphabetical order:")
print(places)

# Task 9
cities = ["Paris", "Tokyo", "New York", "Berlin", "Sydney"]

cities.append("London")
print("After append:", cities)

cities.insert(2, "Barcelona")
print("After insert:", cities)

cities.remove("New York")
print("After remove:", cities)

popped_city = cities.pop()
print("After pop:", cities)
print("Popped city:", popped_city)

cities.clear()
print("After clear:", cities)

cities = ["Paris", "Tokyo", "New York", "Berlin", "Sydney"]

index_of_tokyo = cities.index("Tokyo")
print("Index of Tokyo:", index_of_tokyo)

count_of_paris = cities.count("Paris")
print("Count of Paris:", count_of_paris)

cities.sort()
print("After sort:", cities)

cities.reverse()
print("After reverse:", cities)

cities_copy = cities.copy()
print("Copy of cities:", cities_copy)

sorted_cities = sorted(cities)
print("Sorted cities:", sorted_cities)

print("Original list after sorted() operation:", cities)

# Task 10
cities = ["Paris", "Tokyo", "New York", "Berlin", "Sydney"]

print("List of cities:", cities)

# print("List of cities", cities[10])
print("List of cities", cities[1])

