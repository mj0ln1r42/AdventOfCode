import argparse

def main(filename, top_n):
    counts = []
    with open(filename) as f:
        current = 0
        for _, line in enumerate(f):
            if not line.strip():
                counts.append(current)
                current = 0
                continue
            current += int(line.strip())
    counts = sorted(counts, reverse=True)
    print(sum(counts[:int(top_n):]))



if __name__ == '__main__':
    # Example Run:
    # python -m 2022.day1_1 -f 'inputs/day1_1.txt' -n 1
    parser = argparse.ArgumentParser(
        description='Advent of Code 2022, Day 1, puzzle 1')

    parser.add_argument(
        '-f',
        '--file',
        dest='filename',
        help='The input file',
        required=True)

    parser.add_argument(
        '-n',
        '--top-n',
        dest='top_n',
        help='The number of top sums to ... sum',
        required=True)
        
    args = parser.parse_args()
    
    main(args.filename, args.top_n)
