# I have a house. The house has 15 bricks.
bricks = 15

# Print out how many bricks I have.
print("bricks1 " + str(bricks))

# A builder comes and builds more, and multiplies the amount of bricks by 5.
bricks *= 5

# Print out how many bricks I have.
print("bricks2 " + str(bricks))

# A group teeenagers come, and smash of the bricks. They smash 1/6 of the bricks. Bricks MUST be integers.
brickSmashed = bricks // 6
bricks -= brickSmashed

# Print the bricks.
print("bricks3 " + str(bricks))
