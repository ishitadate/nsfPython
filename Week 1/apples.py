# Steve starts with 6 apples
apples = 6

# He eats 3
apples = apples - 3

# He gives away 1/3 of the remaining apples
apples = apples - (apples // 3)

# He goes to the store. The store has 10 apples and he buys half of them
stareApples = 10
apples = apples + (stareApples // 2)

# He has twice as many bananas as apples
bananas = apples * 2

# How many bananas does he have?
print(bananas)