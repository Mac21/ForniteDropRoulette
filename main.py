import random


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

invalid_locations = [
    ('a', 7), ('a', 8), ('a', 9), ('a', 10),
    ('b', 1), ('b', 8), ('b', 9), ('b', 10),
    ('c', 8), ('c', 9), ('c', 10),
    ('d', 10),
    ('e', 1),
    ('f', 1),
    ('g', 1),
    ('h', 1), ('h', 10),
    ('i', 1), ('i', 10),
    ('j', 1), ('j', 2), ('j', 9), ('j', 10),
]


def get_location():
    return random.choice(letters), random.choice(numbers)


def main():
    while True:
        loc = get_location()
        if loc not in invalid_locations:
            print(loc)
            break


if __name__ == "__main__":
    main()
