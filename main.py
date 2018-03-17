import random


letters = [chr(x) for x in range(97, 107)]
locations = [(y, i+1) for i, l in enumerate(letters) for y in letters]

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


def main():
    while True:
        choice = input("(r)oll | (q)uit")
        if choice.lower() == 'r':
            loc = random.choice(locations)
            if loc not in invalid_locations:
                print(loc)
        elif choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()
