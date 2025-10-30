# https://adventofcode.com/2015/day/4

import hashlib

input_data = "iwrupvqb"


def advent_coins(key):

    i = 1

    while True:
        wallet = key + str(i)
        hash_bytes = hashlib.md5(wallet.encode())
        hash_hex = hash_bytes.hexdigest()

        # For part 1
        # if hash_hex.startswith("00000"):
        # For part 2
        if hash_hex.startswith("000000"):
            print(hash_hex)
            break
        else:
            i += 1

    return i


print(advent_coins(input_data))
