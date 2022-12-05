from puzzle_info import PuzzleInfo

def get_intersecting_item(*args):
    inter = None
    for s in args:
        if inter is None:
            inter = set(s)
        else:
            inter &= set(s)

    return min(inter)


def get_extra_item(line):
        length = len(line)
        half = int(length/2)

        first = line[0:half]
        second = line[half:length]

        item = get_intersecting_item(first, second)
        return item


def item_to_priority(item):
    priority = ord(item)
    if priority > ord('a'):
        priority = priority - ord('a') + 1
    else:
        priority = priority - ord('A') + 27

    return priority


if __name__ == '__main__':
    info = PuzzleInfo()
    sum = 0
    group=[]
    for line in info.input_lines:
        # for pt.1
        # item = get_extra_item(line)

        # for pt.2
        group += [line]
        if len(group) == 3:
            item = get_intersecting_item(*group)
            group = []
            priority = item_to_priority(item)
            sum += priority

    print(sum)
