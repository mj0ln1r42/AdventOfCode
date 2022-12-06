from puzzle_info import PuzzleInfo


def is_subset(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a <= set_b or set_b <= set_a

def overlap(a, b):
    return len(set(a).intersection(b)) > 0

def string_to_range(words):
    first, last = words.split('-')
    return range(int(first), int(last)+1)

def get_line_points(line):
    first, second = line.split(',')
    range_a = string_to_range(first)
    range_b = string_to_range(second)
    # Pt.1
    #return 1 if is_subset(range_a, range_b) else 0

    # Pt.2
    return 1 if overlap(range_a, range_b) else 0

if __name__ == '__main__':
    info = PuzzleInfo()
    sum = 0
    for line in info.input_lines:
        # Do whatever with each line
        sum += get_line_points(line)

    print(sum)
