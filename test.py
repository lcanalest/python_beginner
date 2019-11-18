# Lists Functions
lst_friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi"]
lst_numbers = [42, 13, 56, 41, 4]
lst_friends.extend(lst_numbers) # Copy list lst_numbers to lst_friends
print(lst_friends)

lst_friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi"]
lst_numbers = [42, 13, 56, 41, 4]
lst_friends.append("Pepe")
lst_friends.sort()
print(lst_friends)

lst_friends.sort(reverse=True)
print(lst_friends)

lst_friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi", "Pepe"]
lst_friends.reverse()
print(lst_friends)

lst_friends.remove("Donald")
print(lst_friends)

lst_friends.pop() # Pops out the last item in the list
print(lst_friends)

lst_friends = ["Hugo", "Paco", "Luis", "Donald", "Daysi", "Pepe"]
print("Index: " + str(lst_friends.index("Daysi")))

lst_friends.append("Daysi")
print(len(lst_friends))
print(lst_friends.count("Daysi"))
print("Index: " + str(lst_friends.index("Daysi")))

lst_friends_2 = lst_friends.copy()
print(lst_friends_2)

lst_friends_2.clear()
print(lst_friends_2)

# Tuples
coordinates = (111, 2222)
print(coordinates[0])
coordinates[0] = 1333 # Tuples are very similar to list, but they can't be modified, they're inmutable