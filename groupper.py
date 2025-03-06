#/usr/bin/env python3
import sys
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("-c", "--count", dest="count", type=int, metavar="", help="Cont of group elements")
    parser.add_argument("-j", "--join", dest="join_values", metavar="", help="Joining the groupped values")

    return parser.parse_args()

def print_group(group, joining, join_string):
    if joining:
        print(join_string.join(group))
    else:
        for i in group:
            print(i)
    print()

def main():
    args = parse_arguments()

    group_count = 100
    join_string = " "
    joining = False

    if args.join_values:
        join_string = args.join_values
        joining = True
    if args.count:
        group_count = args.count


    group = []
    for line in sys.stdin.buffer:
        try:
            decoded_line = line.decode("utf-8").strip()  # Próbáld UTF-8-ként dekódolni
        except UnicodeDecodeError:
            decoded_line = line.decode("latin-1", errors="replace").strip()
        
        if len(group) < group_count:
            group.append(decoded_line)
        else:
            print_group(group, joining, join_string)
            group.clear()
    
    if len(group) > 0:
        print_group(group, joining, join_string)
    

if __name__ == '__main__':
    main()