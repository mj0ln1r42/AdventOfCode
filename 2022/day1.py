from argparse import ArgumentParser
from puzzle_info import PuzzleInfo

if __name__ == '__main__':
    # Example Run:
    # python -m day1 -n 3
    parser = ArgumentParser()
    parser.add_argument(
        '-n',
        '--top-n',
        dest='top_n',
        help='The number of top sums to ... sum',
        required=False,
        type=int,
        default=1)

    info = PuzzleInfo(parser)

    counts = []
    current = 0
    for line in info.input_lines:
        if not line.strip():
            counts.append(current)
            current = 0
            continue
        current += int(line.strip())
    counts.append(current)
    counts = sorted(counts, reverse=True)
    print(sum(counts[:info.args.top_n:]))
