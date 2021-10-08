side_a = ["buyer", "goat", "grass", "dog"]

side_b = []

boat = []

def load_boat(item):
    boat.append(item)

def offload_boat(item):
    boat.remove(item)

# down
def trip_1(side_a, side_b):
    for item in side_a:
        if item == 'buyer':
            load_boat('buyer')
        if item == 'goat':
            load_boat('goat')
    side_a.remove('buyer')
    side_a.remove('goat')
    print("The boat has the following members: \n {}".format(boat))
# up
def trip_2(side_a, side_b):
    for item in side_b:
        if item == 'buyer':
            load_boat('buyer')
            side_b.remove('buyer')
    print("The boat has the following members: \n {}".format(boat))
# down
def trip_3(side_a, side_b):
    for item in side_a:
        if item == 'buyer':
            load_boat('buyer')
        elif item == 'grass':
            load_boat('grass')
    side_a.remove('buyer')
    side_a.remove('grass')
    print("The boat has the following members: \n {}".format(boat))
# up
def trip_4(side_a, side_b):
    for item in side_b:
        if item == 'buyer':
            load_boat('buyer')
        elif item == 'goat':
            load_boat('goat')
    side_b.remove('buyer')
    side_b.remove('goat')
    print("The boat has the following members: \n {}".format(boat))
# down
def trip_5(side_a, side_b):
    for item in side_a:
        if item == 'buyer':
            load_boat('buyer')
        elif item == 'dog':
            load_boat('dog')
    side_a.remove('buyer')
    side_a.remove('dog')
    print("The boat has the following members: \n {}".format(boat))
# up
def trip_6(side_a, side_b):
    for item in side_b:
        if item == 'buyer':
            load_boat('buyer')
            side_b.remove('buyer')
# Down
def trip_7(side_a, side_b):
    for item in side_a:
        if item == 'buyer':
            load_boat('buyer')
        elif item == 'goat':
            load_boat('goat')
    side_a.remove('buyer')
    side_a.remove('goat')
    print("The boat has the following members: \n {}".format(boat))

# Tuanze safari wadau
# hii ni trip 1
print("~~~~~~~~~~~~~~~~~~Trip 1 => down~~~~~~~~~~~~~~~~~~")
trip_1(side_a, side_b)
print("This is side a {}".format(side_a))
for x in boat:
    side_b.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side b {}".format(side_b))
print("**************************************************")

# trip 2
print("~~~~~~~~~~~~~~~~~~Trip 2 => up~~~~~~~~~~~~~~~~~~")
trip_2(side_a, side_b)
print("This is side b {}".format(side_b))
for x in boat:
    side_a.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side a {}".format(side_a))
print("**************************************************")

# trip 3
print("~~~~~~~~~~~~~~~~~~Trip 3 => down~~~~~~~~~~~~~~~~~~")
trip_3(side_a, side_b)
print("This is side a {}".format(side_a))
for x in boat:
    side_b.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side b {}".format(side_b))
print("**************************************************")

# trip 4
print("~~~~~~~~~~~~~~~~~~Trip 4 => up~~~~~~~~~~~~~~~~~~")
trip_4(side_a, side_b)
print("This is side b {}".format(side_b))
for x in boat:
    side_a.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side a {}".format(side_a))
print("**************************************************")

# trip 5
print("~~~~~~~~~~~~~~~~~~Trip 5 => down~~~~~~~~~~~~~~~~~~")
trip_5(side_a, side_b)
print("This is side a {}".format(side_a))
for x in boat:
    side_b.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side b {}".format(side_b))
print("**************************************************")

# trip 6
print("~~~~~~~~~~~~~~~~~~Trip 6 => up~~~~~~~~~~~~~~~~~~")
trip_6(side_a, side_b)
print("This is side b {}".format(side_b))
for x in boat:
    side_a.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side a {}".format(side_a))
print("*************************************************")

# trip 7
print("~~~~~~~~~~~~~~~~~~Trip 7 => down~~~~~~~~~~~~~~~~~~")
trip_7(side_a, side_b)
print("This is side a {}".format(side_a))
for x in boat:
    side_b.append(x)
boat.clear()
print("After arrival of the boat")
print("This is side b {}".format(side_b))
print("**************************************************")
