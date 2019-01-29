from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

# Printing the Welcome Message
print_welcome()

# Write code to insert food types into a data structure here. The data is in data.py
types_trie = Trie()
types_trie.add_list_values(types)

# Write code to insert restaurant data into a data structure here. The data is in data.py
restaurants_hash = HashMap(len(restaurant_data))

while (len(restaurant_data))>0:
    templist = []
    typename = restaurant_data[0][0]
    typelist = LinkedList()
    typelist.remove_node(None)
    for restaurant in restaurant_data:
        if restaurant[0] == typename:
            rest_hash = HashMap(len(restaurant))
            rest_hash.assign("name", restaurant[1])
            rest_hash.assign("price", restaurant[2])
            rest_hash.assign("rating", restaurant[3])
            rest_hash.assign("address", restaurant[4])
            typelist.insert_beginning(rest_hash)
        else:
            templist.append(restaurant)
    restaurants_hash.assign(typename, typelist)
    restaurant_data = templist

def proceed():
    while True:
        user_input3 = str(input("\nShow restaurants for this food type? Type 'y' for Yes or 'n' for No.\n")).lower()
        if user_input3 == 'y':
            return True
        elif user_input3 == 'n':
            return False
        else:
            print("Invalid entry. Please enter 'y' or 'n'")

# Write code for user interaction here
while True:
    valid_input = False
    while not valid_input:
        user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
        valid_input = types_trie.return_possibilities(user_input)
        if not valid_input:
            print("\nNo results found. Please try again...")

    while len(valid_input) > 1:
        print("\nMultiple results found:")
        for restaurant_type in valid_input:
            print(restaurant_type)
        user_input2 = str(input("\nPlease enter more letters.\n")).lower()
        valid_input = types_trie.return_possibilities(user_input2)
    print("\nSingle result found:")
    print(valid_input[0])

    # After finding food type write code for retrieving restaurant data here
    if proceed():
        print("\nDisplaying restaurant information...")
        selected_restaurants = restaurants_hash.retrieve(valid_input[0])
        node = selected_restaurants.get_head_node()
        while node:
            rest = node.get_value()
            print("\n******************************")
            print("Name: " + rest.retrieve("name"))
            print("Price: " + rest.retrieve("price"))
            print("Rating: " + rest.retrieve("rating"))
            print("Address: " + rest.retrieve("address"))
            node = node.get_next_node()

    user_input4 = str(input("\nSearch again? Enter y or n.\n")).lower()
    if user_input4 == 'y':
        pass
    elif user_input4 == 'n':
        break
    else:
        print("Invalid entry. Restarting search...\n")