f = open("bytes.txt", "r").read().strip()

print f.decode("hex")


# Decoding the hex, we get something like this:
# geo:40.6944,73.9866
# These are coordinates, but not in Brooklyn. Turns out we need to negate the second coordinate to get 40.6944,-73.9866

# Using google maps, we see that NYU Tandon is very close by, and since HSF is organized by NYU, it can't be a coincidence.
# The flag is NYU Tandon School of Engineering
