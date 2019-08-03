# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.

import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
setup= """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

# for l in locations:
#     print(locations[l])
# value for value in list1 if value in list2
#     value for value in (l for l in locations if 'forest' in locations[l]) if value in [e for e in exits if value in e.values()]
#         value
#         value for value in (e.values() for e in exits if  e.) (l for l in locations if 'forest' in locations[l]) if value in [e for e in exits if
#                                                                                      value in e.values()]



# print([(l, locations[l]) for l in exits for f in locations if 'forest' in locations[f] if f in exits[l].values()])

def loop_comp():
    for loc in sorted(locations):
        for l in ([(l, locations[l]) for l in exits if loc in exits[l].values() ]):
            print(f"Locations leading to {loc}", end='\t')
            print(l)



def nested_comp():
    locs = [f"Locations leading to {loc}{(l, locations[l])}" for l in exits for loc in sorted(locations) if loc in exits[l].values() ]
    print(locs)

def nested_gen():
    for locs in (f"Locations leading to {loc}{(l, locations[l])}" for l in exits for loc in sorted(locations) if loc in exits[l].values()):
        print(locs)



# forest=[]
# for l in exits:
#     for f in locations:
#         if 'forest' in locations[f]:
#             if f in exits[l].values():
#                 forest.append((l,locations[l]))
# print(forest)

def nested_loop():
    for loc in sorted(locations):
        for l in exits:
             if loc in exits[l].values():
                print(f"Locations leading to {loc}", end='\t')
                print((l, locations[l]))

result1 = timeit.timeit(loop_comp, setup, number=10000)
result2 =  timeit.timeit(nested_comp, setup, number=10000)
result3 = timeit.timeit(nested_loop, setup, number=10000)
result4 = timeit.timeit(nested_gen, setup, number=10000)

print(f"Loop comp:\t{result1}")
print(f"Nested comp:\t{result2}")
print(f"Nested gen:\t{result4}")
print(f"Nested Loop:\t{result3}")

