import inspect
import re
from argparse import ArgumentParser
from pathlib import Path

class PuzzleInfo():
    def __init__(self, arg_parser = ArgumentParser()):
        *_, callsite = filter(lambda frame: "AdventOfCode" in frame.filename, inspect.stack())
        input_file = Path('inputs') / f'{Path(callsite.filename).stem}.txt'

        self._day_num = re.search(r'[^\d]*(\d[^\.]*)', input_file.stem).group(1)

        # Example Run:
        # python -m day%%
        arg_parser = ArgumentParser(
            description=f'Advent of Code 2022, Day {self._day_num}',
            parents=[arg_parser],
            add_help=False)

        arg_parser.add_argument(
            '-f',
            '--file',
            dest='filename',
            help='The input file',
            type=Path,
            default=input_file)
        
        self.args = arg_parser.parse_args()

        print(f'reading {self.args.filename}...')
        with open(self.args.filename) as f:
            self.input_lines = f.readlines()
