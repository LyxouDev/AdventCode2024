
######################################
# Première/Deuxième Etoile - Jour 24 #
######################################

def count_heights(lines):
    return [r.count('#') for r in zip(*lines)]


def read_input(input):
    keys, locks = [], []
    with open('input.txt') as f:
        for block in f.read().strip().split('\n\n'):
            lines = block.strip().split('\n')
            if lines[0] == '#####':
                keys.append(count_heights(lines))
            else:
                locks.append(count_heights(lines))
    return keys, locks


def fits(key, lock):
    return all(y1 + y2 <= 7 for (y1, y2) in zip(key, lock))


def part1(keys, locks):
    return sum(fits(key, lock) for key in keys for lock in locks)


def main(input_file):
    keys, locks = read_input(input_file)
    print(part1(keys, locks))


if __name__ == '__main__':
    import sys
    import os.path
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = os.path.abspath(os.path.join(__file__, '..', 'input'))

    main(input_file)
